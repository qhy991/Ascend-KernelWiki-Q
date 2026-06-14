---
id: wiki-technique-triton-ascend-opt
title: "Triton Optimization for Ascend NPUs"
type: wiki-technique
architectures: [ascend910, ascend910b]
tags: [triton, pipeline-scheduling, cube-unit, unified-buffer]
confidence: verified
sources: [doc-ascendc-api-reference]
---

# Triton Optimization for Ascend NPUs

Optimizing Triton kernels for Ascend requires understanding the underlying AICore architecture. The two most critical units are the **Cube Unit** (for matrix multiplication) and the **Unified Buffer (UB)** / **L1 Buffer** (for memory management).

## 1. Block Size Alignment for Cube Unit

The Cube unit heavily relies on the **Fractal (NZ) format**. In Ascend hardware, data chunks processed by the Cube unit operate efficiently on 16x16 blocks (specifically for fp16 data).

When using `tl.dot(a, b)`, Triton will partition the matrices into blocks of `BLOCK_M`, `BLOCK_N`, and `BLOCK_K`.

**Optimization Rule:**
Always ensure that `BLOCK_M`, `BLOCK_N`, and `BLOCK_K` are multiples of **16**. 
- If you use unaligned block sizes (e.g., `BLOCK_M=13`), the Triton compiler must insert padding and masking operations before feeding data into the Cube unit. 
- This padding introduces significant overhead, wasting both compute cycles and Unified Buffer memory bandwidth.

```python
# Bad for Ascend
@triton.jit
def gemm(..., BLOCK_M: tl.constexpr = 24, ...):
    ...
    
# Good for Ascend
@triton.jit
def gemm(..., BLOCK_M: tl.constexpr = 32, ...):
    ...
```

## 2. Tuning `num_stages` (Pipeline Depth)

In Triton, `num_stages` dictates the depth of the software pipeline (how many blocks are pre-fetched into shared memory).

On NVIDIA, this maps to allocating multiple buffers in Shared Memory and using `cp.async` to asynchronously load them.
On Ascend, this maps to the number of buffers allocated in the **Unified Buffer (UB)** or **L1 Buffer**, which enables **Ping-Pong or Multi-buffering** overlapping the MTE (Memory Transfer Engine) and compute units.

**Optimization Rule:**
- **Increase `num_stages`** (e.g., 3, 4, or 5) for compute-bound kernels (like GEMM) to ensure the Cube unit is never starved waiting for data.
- **Watch the Memory Limits**: Ascend NPUs have specific limits on UB size (e.g., ~1MB on 910B) and L1 size. If `BLOCK_M * BLOCK_K * num_stages * sizeof(dtype)` exceeds available capacity, the compiler will fail to allocate the buffers or spill heavily, ruining performance. You often have to balance large `BLOCK` sizes against a higher `num_stages`.

## 3. Coalesced Memory Accesses

Ascend's memory transfer engine (MTE2/MTE3) prefers contiguous, 32-byte aligned memory bursts.

When loading blocks in Triton:
```python
offs_am = (pid_m * BLOCK_M + tl.arange(0, BLOCK_M)) % M
offs_k = tl.arange(0, BLOCK_K)
a_ptrs = a_ptr + (offs_am[:, None] * stride_am + offs_k[None, :] * stride_ak)
a = tl.load(a_ptrs, mask=...)
```

Ensure that the inner-most dimension being loaded is contiguous in Global Memory. The Ascend compiler will attempt to generate `DataCopy` instructions (bulk memory transfers) instead of scalar loads. If the access is scattered, it will fall back to inefficient gathering.

## 4. Avoiding Complex Control Flow

The Vector unit on Ascend is a powerful SIMD machine, but complex data-dependent branching (`if/else` on vector elements) can cause instruction cache misses and serialization. Use `tl.where` (which maps to a `Select` instruction on Ascend) instead of Python-level branching whenever possible.
