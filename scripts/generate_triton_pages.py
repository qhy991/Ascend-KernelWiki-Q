import os

wiki_languages_path = "/Users/haiyan-mini/Agent4Kernel/ascend-kernelwiki-q/wiki/languages"
wiki_techniques_path = "/Users/haiyan-mini/Agent4Kernel/ascend-kernelwiki-q/wiki/techniques"

triton_guide_content = """---
id: wiki-language-triton-ascend
title: "Triton for Ascend: Language Guide & Differences"
type: wiki-language
architectures: [ascend910, ascend910b]
tags: [triton, ascendc, ptx, python]
confidence: verified
sources: [doc-ascendc-api-reference]
---

# Triton for Ascend (`triton_ascend`)

Triton provides a Python-based abstraction for writing high-performance kernels. The Huawei Ascend port of Triton (`triton_ascend` or standard `triton` on Ascend PyTorch) translates Triton's intermediate representation (IR) directly down to Ascend's LLVM IR, ultimately generating an ELF for the AICore.

While standard Triton code is largely portable, relying too heavily on NVIDIA GPU (PTX) specifics will cause issues. 

## Architectural Mapping

| Triton Concept | NVIDIA (CUDA) Backend | Ascend Backend |
|----------------|-----------------------|----------------|
| `tl.dot()` | Tensor Cores (`mma` / `wmma`) | Cube Unit (`matmul`) |
| Element-wise Ops | CUDA Cores (SIMT lanes) | Vector Unit (SIMD instructions) |
| Shared Memory | Shared Memory (L1 / SMEM) | Unified Buffer (UB) & L1 Buffer |
| `num_warps` | Threads per block / 32 | Translates to SIMD block splitting or mapping configuration (Not literally 32 threads) |
| Core execution | Streaming Multiprocessor (SM) | AICore |

## Key Differences & Limitations

### 1. No Inline PTX Assembly
Triton provides `tl.inline_asm_elementwise` to let developers write raw PTX assembly for operations Triton doesn't natively support.
- **Ascend limitation**: PTX assembly cannot run on Ascend. If your kernel contains `tl.inline_asm_elementwise("cvt.rn.bf16.fp32 ...")`, it will fail to compile.
- **Solution**: Stick to native Triton math functions (`tl.math.*`), which the Ascend compiler natively lowers to Vector Unit instructions.

### 2. The Meaning of `num_warps`
On NVIDIA, `num_warps=4` strictly means a thread block will consist of 128 threads (4 * 32). Triton auto-parallelizes data chunks across these 128 threads.
On Ascend, there is no direct equivalent to a 32-thread "Warp" execution model. Instead, `num_warps` acts as a tuning knob that influences how the Triton compiler tiles and maps operations across the AICore's parallel execution units. You should treat `num_warps` purely as an abstract parallelism parameter when tuning for Ascend.

### 3. Data Layout Management
When doing `tl.dot()`, NVIDIA Tensor Cores expect specific layouts. Triton hides this layout conversion using Shared Memory swizzling.
On Ascend, the Cube unit strictly requires the data to be in **NZ (Fractal) Format**. The Ascend Triton backend implicitly inserts layout conversion routines (ND -> NZ) into the generated LLVM IR before hitting the Cube unit. You don't write this conversion, but you must be aware of its overhead.

### 4. Mathematical Functions
Ascend NPU has native instructions for most math operations. However, depending on the exact driver version and Triton backend version, some exotic math ops might fall back to emulation or fail. Generally, `tl.math.exp`, `tl.math.sin`, `tl.math.cos`, etc. are fully supported on the Vector unit.

## Best Practices

- **Write Portable Triton**: Do not hardcode NVIDIA-specific logic or PTX.
- **Profile Regularly**: Use `msprof` to inspect the generated Ascend kernel. You might find that the generated code struggles with heavy ND-to-NZ conversions if block sizes aren't chosen correctly.
"""

triton_opt_content = """---
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
"""

os.makedirs(wiki_languages_path, exist_ok=True)
os.makedirs(wiki_techniques_path, exist_ok=True)

with open(os.path.join(wiki_languages_path, "triton-ascend-guide.md"), "w") as f:
    f.write(triton_guide_content)

with open(os.path.join(wiki_techniques_path, "triton-ascend-optimization.md"), "w") as f:
    f.write(triton_opt_content)

print("Triton Ascend generation script complete.")
