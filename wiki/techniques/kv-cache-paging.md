---
id: technique-kv-cache-paging
title: "KV Cache Paging — Block-Table Memory Management for NPU Inference"
type: wiki-technique
architectures: [ascend910b]
tags: [kv-cache-paging, paged-attention, inference, memory, optimization]
confidence: source-reported
techniques: [kv-cache-paging]
hardware_features: [global-memory, unified-buffer, mte]
kernel_types: [attention, flash-attention]
related: [kernel-paged-attention-npu, technique-online-softmax, pattern-host-dispatch-bound]
sources: [doc-vllm-ascend, doc-ascend-memory-hierarchy]
reproducibility: concept
---

KV cache paging is the memory-management half of paged attention: instead of storing each sequence's key/value tensors as one contiguous Global Memory (GM) region, the cache is carved into fixed-size physical blocks and a per-sequence block table maps logical token positions to physical block ids. This lets an inference server pack many variable-length sequences into GM with under 4% waste, where a contiguous cache typically wastes 60-80% to fragmentation and over-reservation. The attention kernel then gathers exactly the blocks a sequence needs via the block table, so the paging layer is invisible to the math (see `kernel-paged-attention-npu`).

## The Problem with a Contiguous KV Cache

A naive cache reserves, per sequence, a contiguous GM buffer sized for `max_seq_len`. Two costs follow:

- **Internal waste**: a sequence that decodes 200 tokens but was reserved for 4096 leaves the remaining slots allocated but unused for its entire lifetime.
- **External fragmentation**: as sequences of different lengths finish and free their buffers, GM is left with holes too small to host the next request, even when total free bytes are sufficient.

Together these push effective utilization down to the 20-40% range. Paging replaces one big reservation per sequence with many small, uniformly-sized, freely-relocatable blocks, which removes external fragmentation entirely and caps internal waste at one partial block per sequence.

## Block Layout in Global Memory

The KV cache is a flat pool of `num_blocks` physical blocks, each holding `block_size` tokens (commonly **128**) of keys and of values. With `block_table[seq] -> [phys_block_ids]`, logical token `t` of a sequence lives in physical block `block_table[seq][t / block_size]` at intra-block offset `t % block_size`.

```
Logical view (sequence A, 300 tokens, block_size=128):
  tokens [0..127] [128..255] [256..299|pad]
            │          │           │
block_table[A] = [ 7,         2,          5 ]   # physical block ids
            │          │           │
Physical GM pool:
  blk0 blk1 [blk2←A1] blk3 blk4 [blk5←A2] blk6 [blk7←A0] ...
```

Only block 5 (A's last block) is partially filled; everything else is fully packed. The physical blocks for one sequence need not be adjacent or ordered, which is exactly what frees the allocator from fragmentation.

## The Block Allocator

A central allocator owns the free list of physical block ids. Its contract is small:

- **Allocate**: when a sequence needs room for new tokens (prefill, or every `block_size`-th decode step), it requests blocks; the allocator pops ids off the free list and appends them to `block_table[seq]`.
- **Free**: when a sequence finishes (EOS or eviction), all of its physical blocks are returned to the free list and become immediately reusable by any other sequence.

```python
class BlockAllocator:
    def __init__(self, num_blocks, block_size=128):
        self.block_size = block_size
        self.free = list(range(num_blocks))   # free physical block ids
        self.ref = [0] * num_blocks           # ref counts for sharing

    def allocate(self, n):
        if len(self.free) < n:
            raise OutOfBlocks(n, len(self.free))
        blocks = [self.free.pop() for _ in range(n)]
        for b in blocks:
            self.ref[b] = 1
        return blocks

    def free_seq(self, block_ids):
        for b in block_ids:
            self.ref[b] -= 1
            if self.ref[b] == 0:
                self.free.append(b)           # reusable immediately

    def blocks_needed(self, num_tokens):
        return (num_tokens + self.block_size - 1) // self.block_size
```

Because blocks are uniform, the free list is a plain stack — allocation and free are O(1) and never search for a hole. This allocator lives on the host (see `pattern-host-dispatch-bound`); only the resulting `block_table` is shipped to the device.

## Prefix Sharing via Copy-on-Write

Many requests share a common prefix — a system prompt, a few-shot preamble, or a beam-search parent. Paging shares the *physical* blocks of that prefix across sequences by reference-counting them, so the KV for a shared prefix is computed and stored once.

- On fork, the new sequence's `block_table` points at the same prefix block ids and each shared block's ref count is incremented.
- A block stays read-only while `ref > 1`. When a sequence must write into a shared block (it diverges mid-block), the allocator performs **copy-on-write**: allocate a fresh block, copy the shared block's valid tokens into it, redirect this sequence's `block_table` entry, and decrement the original's ref count.
- Fully-shared (untouched) prefix blocks are never duplicated, so N sequences sharing a 2K-token prompt cost one copy of that prompt's KV, not N.

This is why `free_seq` decrements rather than unconditionally releasing: a block returns to the free list only when its last referencing sequence is done.

## How the Attention Kernel Gathers Blocks

The kernel never sees the pool layout — it sees a sequence's `block_table` row and walks it. For each logical block it resolves the physical id, then uses the Memory Transfer Engine (**MTE**) to copy that block's K and V from GM into Unified Buffer (UB), where the attention math runs (online softmax, see `technique-online-softmax`).

```cpp
// Per-sequence paged-attention gather (conceptual)
void PagedAttentionGather(const int* block_table,   // physical ids for this seq
                          int num_logical_blocks,
                          int block_size,
                          GM_ADDR k_cache, GM_ADDR v_cache) {
    for (int lb = 0; lb < num_logical_blocks; lb++) {
        int phys = block_table[lb];                 // logical -> physical
        // MTE-gather one K block and one V block into UB
        GM_ADDR k_src = k_cache + (uint64_t)phys * block_size * head_dim;
        GM_ADDR v_src = v_cache + (uint64_t)phys * block_size * head_dim;
        DataCopy(ubK, k_src, block_size * head_dim);  // MTE: GM -> UB
        DataCopy(ubV, v_src, block_size * head_dim);  // MTE: GM -> UB
        // ... Q·Kᵀ, online-softmax accumulate, ·V on this block in UB ...
    }
}
```

The gather is a scatter/gather of fixed-size, naturally-aligned blocks, which keeps each `DataCopy` (MTE) transfer regular and coalesced despite the physical blocks being scattered across GM. The block table thus turns an irregular logical layout into a sequence of clean block-sized DMAs.

## Contiguous vs. Paged KV Cache

| Aspect                | Contiguous cache            | Paged cache (block table)        |
|-----------------------|-----------------------------|----------------------------------|
| Allocation unit       | One buffer per sequence     | Fixed-size block (e.g. 128 tok)  |
| External fragmentation| High (variable-size holes)  | None (uniform blocks)            |
| Internal waste        | Up to `max_len − used`      | ≤ one partial block per sequence |
| Memory waste (typical)| 60-80%                      | <4%                              |
| Prefix sharing        | Hard (must copy)            | Native via ref-counted blocks    |
| Kernel access         | Direct contiguous DMA       | MTE-gather via block table       |

The <4% figure and 60-80% contrast are reported by `doc-vllm-ascend`; the waste that remains in the paged case is the unfilled tail of each sequence's last block plus the block-table bookkeeping.

## Trade-offs, Pitfalls, and Notes

- **Block size is a tuning knob.** Larger blocks (e.g. 256) mean fewer block-table entries and longer, more efficient MTE transfers, but more internal waste in the partial tail block; smaller blocks reduce tail waste but lengthen the table and add gather overhead. 128 tokens is a common middle ground.
- **Indirection has a cost.** Every gather pays a `block_table` lookup and a non-sequential GM address per logical block. This is cheap relative to the attention compute, but it does make the kernel read an extra index stream the contiguous path does not need.
- **Out-of-blocks is a real failure mode.** When the free list empties under high concurrency, the server must preempt/evict a sequence (free its blocks, recompute later) rather than overrun GM. Capacity planning is in blocks, not sequences.
- **Copy-on-write must be exact.** A CoW that copies stale or padded slots will silently corrupt attention outputs; only the valid token range of the shared block may be copied, and ref counts must be decremented on every fork-then-diverge.
- **Host/device split.** The allocator, block tables, and CoW decisions are host-side bookkeeping; the device kernel only consumes `block_table` and does MTE gathers. This keeps the device kernel stateless across requests but makes the host dispatch path latency-sensitive (`pattern-host-dispatch-bound`).
- **Confidence.** Block sizes, the `block_table[seq] -> [phys_block_ids]` mechanism, ref-counted prefix sharing, and the <4% waste figure are source-reported from `doc-vllm-ascend`; the exact UB tiling and MTE transfer parameters depend on the concrete kernel in `kernel-paged-attention-npu` and the GM/UB capacities in `doc-ascend-memory-hierarchy`.
