---
id: kernel-rope-ascendc
title: "AscendC Rotary Position Embedding (RoPE)"
type: wiki-kernel
architectures: [ascend910b]
tags: [rope, elementwise, attention, vector-unit, ascendc]
confidence: source-reported
kernel_types: [elementwise, attention]
languages: [ascendc]
sources: [pr-vllm-ascend-001, doc-ascendc-api-reference, blog-ascendc-performance-tips]
related: [kernel-flash-attention-npu, kernel-paged-attention-npu, hw-vector-unit]
techniques: [cube-vector-overlap, pipeline-scheduling]
performance_claims:
  - gpu: Ascend 910B
    dtype: fp16
    shape: "seq=4096, heads=32, head_dim=128"
    metric: speedup
    value: 9.36
    utilization: "vs reference rotary path"
    source_id: pr-vllm-ascend-001
---

# AscendC Rotary Position Embedding (RoPE)

Rotary Position Embedding injects positional information into the query and key tensors of an attention block by rotating each consecutive pair of channels by a position-dependent angle, rather than adding a learned bias. On Ascend 910B, RoPE is a purely element-wise, memory-bound operation that lives entirely on the Vector Unit; the `vllm-ascend` project ships a custom fused `rotary_embedding` AscendC kernel that, as reported in issue #802, delivers **9.36x and 8.26x speedups** over the reference rotary path. This page walks through the math, the cos/sin table layout, and why fusing the rotation into one kernel beats the multi-op reference.

## Mathematical Formulation

For a feature vector of dimension `d` at sequence position `pos`, RoPE pairs up channels and rotates each pair `(x_even, x_odd)` by an angle `theta_i` that depends on the pair index `i` and the position:

```
theta_i   = pos / base^(2i / d)          # base is typically 10000
out_even  = x_even * cos(theta_i) - x_odd  * sin(theta_i)
out_odd   = x_odd  * cos(theta_i) + x_even * sin(theta_i)
```

This is a 2D rotation matrix applied to each `(even, odd)` channel pair:

```
| out_even |   | cos(theta_i)  -sin(theta_i) |   | x_even |
| out_odd  | = | sin(theta_i)   cos(theta_i) | * | x_odd  |
```

The angle `theta_i` is independent of the actual tensor values, so `cos(theta_i)` and `sin(theta_i)` can be precomputed once per `(pos, i)` and reused across every head and every batch element. This is the key property the fused kernel exploits.

### Pairing layouts

Two conventions exist for which channels form a pair, and the kernel must match whatever the model was trained with:

| Layout       | Pair definition                       | cos/sin access            | Used by                     |
|--------------|---------------------------------------|---------------------------|-----------------------------|
| Interleaved  | `(x[2i], x[2i+1])`                     | stride-2, neighbors       | GPT-NeoX original interleave|
| Half-split   | `(x[i], x[i + d/2])`                   | first half vs second half | LLaMA / GPT-NeoX-style HF   |

The half-split (rotate-half) layout is the common case in vLLM-served models: the first `d/2` channels are the "even" half and the second `d/2` channels are the "odd" half. It maps cleanly to contiguous AscendC slices, which is why the custom kernel favors it.

## Why a Fused AscendC Kernel Wins

The reference rotary path in a framework typically performs RoPE as a chain of separate tensor ops: gather/build the cos and sin tensors, split the input into two halves, do `x_even * cos`, `x_odd * sin`, a subtract, then the symmetric pair for the odd output, and finally a concat. Each of those ops is a full pass over Global Memory (GM): it reads its inputs from GM and writes its result back to GM. For a `[seq=4096, heads=32, head_dim=128]` fp16 tensor that is many redundant GM round-trips on a fundamentally memory-bound kernel.

The `vllm-ascend` custom kernel collapses this into a single AscendC kernel:

- **One load, one store.** Q (or K) is streamed from GM into the Unified Buffer (UB) once, rotated in place across the Vector Unit, and written back once. The intermediate `x*cos` and `x*sin` products never touch GM.
- **No separate cos/sin gather.** The cos/sin tables are precomputed and cached in UB (or loaded once per tile), so there is no extra GM-resident `index_select`/gather op to materialize per-position cos/sin before the multiply.
- **Vector op fusion.** The two outputs are produced with a short `Mul` / `Sub` / `Mul` / `Add` chain that stays inside UB, keeping the Vector Unit busy instead of stalling on MTE traffic.

Because RoPE is bandwidth-bound, cutting GM traffic from roughly a half-dozen passes to a single read + single write is the dominant source of the reported speedup. (See `blog-ascendc-performance-tips` for the general "fuse element-wise chains to cut GM round-trips" guidance, and `hw-vector-unit` for the Vector Unit op set.)

## AscendC Implementation

The kernel below implements the half-split layout. `cos` and `sin` hold the precomputed `[seq, d/2]` tables; each row is broadcast across the `heads` dimension. The rotation uses only `Mul`, `Sub`, and `Add` from the AscendC Vector API.

```ascendc
// Half-split RoPE: pair (x[i], x[i + d/2]) for i in [0, d/2)
// cos/sin are precomputed [seq_len, half_dim] tables, cached in UB.
extern "C" __global__ void RopeKernel(
    __gm__ half* q,         // [seq_len, heads, head_dim]
    __gm__ half* cos_tab,   // [seq_len, half_dim]  (half_dim = head_dim / 2)
    __gm__ half* sin_tab,   // [seq_len, half_dim]
    __gm__ half* out,       // [seq_len, heads, head_dim]
    int seq_len, int heads, int head_dim) {

    int half_dim = head_dim / 2;
    TPipe pipe;

    // Per-position cos/sin live in UB and are reused across all heads.
    LocalTensor<half> cos_ub = AllocUB<half>(half_dim);
    LocalTensor<half> sin_ub = AllocUB<half>(half_dim);

    // Work buffers for one head's two halves.
    LocalTensor<half> x_even = AllocUB<half>(half_dim);  // x[0 : d/2]
    LocalTensor<half> x_odd  = AllocUB<half>(half_dim);  // x[d/2 : d]
    LocalTensor<half> tmp    = AllocUB<half>(half_dim);
    LocalTensor<half> o_even = AllocUB<half>(half_dim);
    LocalTensor<half> o_odd  = AllocUB<half>(half_dim);

    for (int p = 0; p < seq_len; ++p) {
        // Load this position's cos/sin once; reuse across every head.
        DataCopy(cos_ub, cos_tab + p * half_dim, half_dim);
        DataCopy(sin_ub, sin_tab + p * half_dim, half_dim);

        for (int h = 0; h < heads; ++h) {
            __gm__ half* x_base = q   + (p * heads + h) * head_dim;
            __gm__ half* o_base = out + (p * heads + h) * head_dim;

            // Single GM read of the two halves into UB.
            DataCopy(x_even, x_base,            half_dim);
            DataCopy(x_odd,  x_base + half_dim, half_dim);

            // out_even = x_even * cos - x_odd * sin
            Mul(o_even, x_even, cos_ub, half_dim);   // x_even * cos
            Mul(tmp,    x_odd,  sin_ub, half_dim);    // x_odd  * sin
            Sub(o_even, o_even, tmp,    half_dim);    // even - odd*sin

            // out_odd  = x_odd * cos + x_even * sin
            Mul(o_odd,  x_odd,  cos_ub, half_dim);    // x_odd  * cos
            Mul(tmp,    x_even, sin_ub, half_dim);    // x_even * sin
            Add(o_odd,  o_odd,  tmp,    half_dim);    // odd + even*sin

            // Single GM write of the rotated head.
            DataCopy(o_base,            o_even, half_dim);
            DataCopy(o_base + half_dim, o_odd,  half_dim);
        }
    }
}
```

Each head pays exactly one GM read pair and one GM write pair; the four multiplies, one subtract, and one add all execute inside UB on the Vector Unit. The cos/sin load is hoisted out of the head loop so the `[half_dim]` table row is fetched once per position instead of once per `(position, head)`.

### Interleaved variant

For the interleaved layout the pairing is `(x[2i], x[2i+1])` instead of `(x[i], x[i+d/2])`. The arithmetic is identical, but the load uses a stride-2 `DataCopy` (or a deinterleave step) to gather the even/odd channels into contiguous UB tensors before the same `Mul`/`Sub`/`Add` fusion runs. The half-split layout avoids that gather, which is one more reason it is preferred on the memory-bound path.

## Relationship to torch_npu and the Attention Pipeline

On `torch_npu`, the native fused primitive is `npu_rotary_mul`, which performs the same rotate-and-combine in a single device call; the `vllm-ascend` custom AscendC kernel is the serving-stack equivalent built directly against the Vector API so it can be co-scheduled with the rest of the inference graph. In a typical decode block, RoPE is applied to Q and K immediately before they are consumed by attention, so its output feeds `kernel-flash-attention-npu` (prefill) or `kernel-paged-attention-npu` (paged KV-cache decode). Because RoPE is Vector-only and attention's score matmul is Cube-heavy, the rotation can be overlapped with surrounding Cube work via the queue model described in `technique-cube-vector-overlap` and `technique-pipeline-scheduling`, hiding most of its latency behind the attention matmuls.

## Performance

As reported by `vllm-ascend` (issue #802, `pr-vllm-ascend-001`), the custom fused `rotary_embedding` kernel achieves the following over the reference rotary path:

| Platform     | dtype | Shape                              | Metric  | Speedup | Notes                          |
|--------------|-------|------------------------------------|---------|---------|--------------------------------|
| Ascend 910B  | fp16  | seq=4096, heads=32, head_dim=128   | speedup | 9.36x   | vs reference rotary path       |
| Ascend 910B  | fp16  | (second reported config)           | speedup | 8.26x   | vs reference rotary path       |

These are the speedups reported by the `vllm-ascend` maintainers for their fused kernel; they are not independently re-benchmarked here, consistent with this page's `source-reported` confidence. The magnitude is plausible precisely because the reference path is dominated by redundant GM round-trips that the fused kernel eliminates.

## Trade-offs, Pitfalls, and Notes

- **Layout must match training.** Applying the half-split kernel to a model trained with the interleaved convention (or vice versa) silently corrupts positions. Confirm the model's RoPE convention before selecting the kernel variant.
- **cos/sin precision.** The cos/sin tables are often built in fp32 and cast to fp16 for the multiply. Computing `theta_i` and the trig values in fp32 before casting avoids accumulating angle error at long positions; doing the whole thing in fp16 can drift for large `pos`.
- **UB residency vs. table size.** Caching the full `[seq, d/2]` cos/sin tables in UB is only viable for short sequences. For long contexts, load one position's row per outer-loop iteration (as in the snippet) rather than holding the whole table resident, to stay within Unified Buffer capacity.
- **Don't re-gather cos/sin per head.** A common slowdown is fetching cos/sin inside the head loop. Hoisting the table load to the position loop (reused across all `heads`) is what keeps the kernel memory-traffic-optimal.
- **In-place caution.** Writing `out` over `q` in place is fine only if `o_even`/`o_odd` are fully materialized in UB before the store, since `out_odd` reads the original `x_even`. Reusing input buffers for outputs mid-computation will corrupt the second rotation term.
- **Apply to Q and K, not V.** RoPE rotates queries and keys only; the value tensor is passed through unrotated. Accidentally rotating V is a correctness bug, not a performance one.
