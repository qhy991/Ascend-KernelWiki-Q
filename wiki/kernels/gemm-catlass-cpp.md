---
id: kernel-gemm-catlass-cpp
title: "CATLASS GEMM — C++ Template Matmul on the Cube Unit"
type: wiki-kernel
architectures: [ascend910b]
tags: [matmul, gemm, catlass, cpp, cube-unit]
confidence: source-reported
kernel_types: [matmul, gemm]
languages: [cpp, ascendc]
sources: [blog-catlass-gemm-templates, pr-catlass-001, doc-catlass-framework]
related: [kernel-matmul-ascendc, migration-cutlass-to-catlass, wiki-hardware-cube-unit]
techniques: [nz-tiling, pipeline-scheduling, double-buffering]
performance_claims:
  - gpu: Ascend 910B
    dtype: fp16
    shape: "M=4096, N=4096, K=4096"
    metric: TFLOPS
    value: 256
    utilization: "~80%"
    source_id: doc-catlass-framework
---

# CATLASS GEMM via C++ Templates

CATLASS (Computing And Tensor Layout Abstraction for Ascend) exposes the Cube Unit through a layered C++ template hierarchy, mirroring the way CUTLASS structures GEMM on NVIDIA GPUs. Where `kernel-matmul-ascendc` reaches the Cube via the high-level AscendC `Matmul` API, this page documents the same fp16 GEMM expressed through CATLASS template instantiation, where tile shapes, data layouts, and the ping-pong scheduling policy are all chosen at compile time. The two paths target identical hardware and report the same headline figure: 256 TFLOPS fp16 at ~80% utilization on Ascend 910B.

## Why a Template Layer

The high-level `Matmul` API hides tiling and double-buffering behind a runtime object. CATLASS instead pushes those decisions into the type system, so the compiler can specialize the kernel for a given architecture, tile shape, and dtype. This is the language-diversity counterpart to `kernel-matmul-ascendc`: same Cube hardware, same NZ tiling, but a C++ template dispatch chain in place of an opaque API call. For users coming from NVIDIA, the mapping is documented in `migration-cutlass-to-catlass`.

## Template Instantiation Chain

CATLASS composes a GEMM from five layers, each resolving to the layer below at compile time:

1. **Arch** — `Arch::AtlasA2` selects the Cube/Vector layout and instruction set for the 910B class.
2. **Dispatch policy** — `Gemm::MmadAtlasA2Pingpong<true>` selects the ping-pong (double-buffered) MMAD schedule. The `true` enables the L1/L0 ping-pong path.
3. **Tile shapes** — `L1TileShape` and `L0TileShape`, each a `GemmShape<M, N, K>`, set the L1 (block) and L0 (Cube fragment) tiling.
4. **Operand types** — `AType`, `BType`, `CType`, each a `Gemm::GemmType<half, layout::RowMajor>`, bind element type and memory layout per operand.
5. **Block + kernel** — `Gemm::Block::BlockMmad<...>` binds the policy, shapes, and types into a block-level MMAD; `Gemm::Kernel::BasicMatmul<Mmad, Epilogue, GemmIdentityBlockSwizzle>` wraps it with an epilogue and a block-swizzle for core scheduling.

### Instantiation Snippet

```cpp
#include "catlass/arch/arch.hpp"
#include "catlass/gemm/gemm_type.hpp"
#include "catlass/gemm/dispatch_policy.hpp"
#include "catlass/gemm/block/block_mmad.hpp"
#include "catlass/gemm/kernel/basic_matmul.hpp"
#include "catlass/gemm/tile/tile_swizzle.hpp"
#include "catlass/layout/layout.hpp"

using namespace Catlass;

// 1. Architecture tag for the 910B-class Cube/Vector layout.
using ArchTag = Arch::AtlasA2;

// 2. Dispatch policy: ping-pong = L1/L0 double buffering on the MMAD pipe.
using DispatchPolicy = Gemm::MmadAtlasA2Pingpong<true>;

// 3. L1 (block) and L0 (Cube fragment) tile shapes.
using L1TileShape = GemmShape<128, 256, 256>;
using L0TileShape = GemmShape<128, 256, 64>;

// 4. Operand types: half element, row-major in global memory.
using AType = Gemm::GemmType<half, layout::RowMajor>;
using BType = Gemm::GemmType<half, layout::RowMajor>;
using CType = Gemm::GemmType<half, layout::RowMajor>;

// 5. Block-level MMAD, then the launchable kernel.
using BlockMmad = Gemm::Block::BlockMmad<
    DispatchPolicy, L1TileShape, L0TileShape, AType, BType, CType>;
using BlockEpilogue = void;  // BasicMatmul writes C directly; no fused epilogue.
using BlockSwizzle  = Gemm::Block::GemmIdentityBlockSwizzle<>;

using MatmulKernel = Gemm::Kernel::BasicMatmul<
    BlockMmad, BlockEpilogue, BlockSwizzle>;
```

The chosen `GemmShape` values must keep K and N as multiples of 16 so the operands tile cleanly into the FRACTAL_NZ fragments the Cube Unit consumes; see `technique-nz-tiling` and `hw-cube-unit` for the fractal layout details.

## Host Launch with AscendCL

The host side allocates global memory through AscendCL (`aclrtMalloc` / `aclrtMemcpy`), packs the problem size into a `GemmCoord{M, N, K}`, and launches the kernel across the available AICores. CATLASS uses the AscendC kernel-launch syntax — `<<<blockDim, l2ctrl, stream>>>` — with `aicCoreNum` as the block dimension:

```cpp
// Query the AI Cube core count once at startup.
uint32_t aicCoreNum = /* aclrtGetDeviceProperties → AI Cube core count */;

aclrtStream stream;
aclrtCreateStream(&stream);

// Global memory for A (M×K), B (K×N), C (M×N), all half.
uint8_t *gmA, *gmB, *gmC;
aclrtMalloc(reinterpret_cast<void **>(&gmA), sizeM * sizeK * sizeof(half), ACL_MEM_MALLOC_HUGE_FIRST);
aclrtMalloc(reinterpret_cast<void **>(&gmB), sizeK * sizeN * sizeof(half), ACL_MEM_MALLOC_HUGE_FIRST);
aclrtMalloc(reinterpret_cast<void **>(&gmC), sizeM * sizeN * sizeof(half), ACL_MEM_MALLOC_HUGE_FIRST);

aclrtMemcpy(gmA, /*...*/, ACL_MEMCPY_HOST_TO_DEVICE);
aclrtMemcpy(gmB, /*...*/, ACL_MEMCPY_HOST_TO_DEVICE);

GemmCoord problemShape{M, N, K};

// Launch BasicMatmul across the AI Cube cores on the stream.
MatmulKernel<<<aicCoreNum, nullptr, stream>>>(problemShape, gmA, gmB, gmC);

aclrtSynchronizeStream(stream);
aclrtMemcpy(/* host C */, gmC, /*...*/, ACL_MEMCPY_DEVICE_TO_HOST);
```

The `nullptr` in the launch is the L2 control argument (`l2ctrl`), left unused for the basic kernel. Once launched, `BasicMatmul` partitions the M×N output into L1 tiles via `GemmIdentityBlockSwizzle`, streams A/B fragments into the Cube through the ping-pong L1/L0 buffers, and writes C back to global memory.

## Ping-Pong, Double Buffering, and NZ

The dispatch policy name encodes the scheduling strategy:

- **Ping-pong = double buffering.** `MmadAtlasA2Pingpong<true>` keeps two L1 buffers and two L0 fragments live, so the MTE can copy the next A/B tile while the Cube computes the current MMAD. This is the same `double-buffering` technique used in `kernel-matmul-ascendc`, expressed as a compile-time policy rather than a runtime buffer index.
- **FRACTAL_NZ tiling.** Operands declared `layout::RowMajor` in global memory are re-tiled into FRACTAL_NZ fragments inside L1 before reaching the Cube. The `L1TileShape`/`L0TileShape` choices determine how those fragments map onto the 16×16 Cube partitions (`technique-nz-tiling`).
- **Pipeline scheduling.** Block swizzle plus ping-pong gives the CopyIn→MMAD→CopyOut overlap described in `technique-pipeline-scheduling`.

## Group GEMM Variant for MoE

For Mixture-of-Experts, CATLASS provides a grouped variant (`group_gemm`) that batches per-expert GEMMs with differing M dimensions into a single launch, with the swizzle handling per-group tile assignment. This is the C++ template analogue of the AscendC pattern in `kernel-grouped-gemm-ascendc` and feeds the dispatch path in `kernel-moe-ascendc`; the operand and policy types are shared with the basic kernel, only the kernel wrapper and the per-group problem array differ.

## Performance on Ascend 910B

The basic fp16 kernel matches the figure already reported for the CATLASS path in `kernel-matmul-ascendc`:

| GPU  | Shape (M×N×K)  | Data Type | TFLOPS | Utilization | Notes                          |
|------|----------------|-----------|--------|-------------|--------------------------------|
| 910B | 4096×4096×4096 | fp16      | 256    | ~80%        | Ping-pong (L1/L0 double buffer)|

This is the same compute-bound regime as the high-level API: the template path adds no measured overhead at large shapes because both ultimately drive identical Cube MMAD instructions.

## Trade-offs and Pitfalls

- **Compile-time rigidity.** Tile shapes and dtypes are template parameters, so each shape/dtype combination compiles to a distinct kernel. This is faster but less flexible than the runtime `Matmul` API in `kernel-matmul-ascendc`; cover the common shapes with explicit instantiations.
- **Tile-shape alignment.** `GemmShape` N and K dimensions must align to the FRACTAL_NZ fragment size (multiples of 16). Misaligned shapes either fail to instantiate or pad, wasting Cube cycles.
- **`aicCoreNum` correctness.** The launch block dimension must be the AI Cube core count, not the total core count. Over-subscribing degrades the swizzle's tile partitioning.
- **L2 control argument.** Passing `nullptr` for `l2ctrl` disables explicit L2 cache hints; for memory-bound shapes a tuned control struct can help, but it is not needed for the compute-bound 4096³ case.
- **Epilogue is unfused here.** `BasicMatmul` writes C directly. Bias/activation fusion requires a non-void `BlockEpilogue`, which changes the instantiation and the per-tile cost.

## Comparison with the High-Level API

| Aspect              | CATLASS C++ templates (this page) | AscendC `Matmul` API (`kernel-matmul-ascendc`) |
|---------------------|-----------------------------------|------------------------------------------------|
| Tiling decision     | Compile-time (`GemmShape`)        | Runtime (tiling object)                        |
| Double buffering    | `MmadAtlasA2Pingpong<true>`       | Runtime buffer index                           |
| Operand layout      | `GemmType<half, RowMajor>`        | `DataCopy` with NZ conversion                  |
| Launch              | `BasicMatmul<<<aicCoreNum,...>>>` | `__global__ __aicore__` entry                  |
| Flexibility         | Lower (per-shape instantiation)   | Higher (one kernel, runtime shapes)            |
| fp16 4096³ peak     | 256 TFLOPS / ~80%                 | 256 TFLOPS / ~80%                              |

## Related Pages

- [AscendC Matmul](kernel-matmul-ascendc) — same GEMM via the high-level runtime API
- [CUTLASS → CATLASS migration](migration-cutlass-to-catlass) — template-chain mapping from NVIDIA
- [Cube Unit](hw-cube-unit) — the MMAD hardware and FRACTAL_NZ fragment layout
