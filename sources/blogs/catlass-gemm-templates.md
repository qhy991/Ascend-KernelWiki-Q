---
id: blog-catlass-gemm-templates
title: "CATLASS — C++ Template GEMM Kernels for Ascend (CUTLASS-style)"
type: source-blog
author: ascend-catlass
date: '2026-03-12'
url: https://gitee.com/ascend/catlass
architectures: [ascend910b]
tags: [catlass, cpp, gemm, matmul, template]
techniques: [nz-tiling, pipeline-scheduling, double-buffering]
hardware_features: [cube-unit, nz-format, l1-buffer, l0-buffer]
kernel_types: [matmul, gemm]
languages: [cpp, ascendc]
confidence: source-reported
---

# CATLASS — C++ Template GEMM Kernels for Ascend

CATLASS is a CUTLASS-style C++ template library for building high-performance GEMM kernels on Ascend NPUs. It mirrors the layered, header-only design philosophy familiar to CUDA developers: you compose a kernel from architecture, dispatch-policy, tile-shape, and data-type template parameters rather than hand-writing a monolithic AscendC kernel. The result is reusable matmul building blocks that target the Cube unit on Atlas A2 (Ascend 910B) hardware.

## Why a Template Library

Hand-written AscendC matmul kernels (see kernel-matmul-ascendc) tightly couple tiling, pipeline scheduling, and format handling into one file. Every new shape, dtype, or fusion variant means another copy. CATLASS factors these decisions into composable template parameters, so a single instantiation expresses a fully tuned kernel:

- **Reuse** — one `BlockMmad` body serves many tile shapes and dtypes.
- **Tuning** — swap a dispatch policy or tile shape without touching kernel logic.
- **Familiarity** — the layering maps almost one-to-one onto CUTLASS concepts, easing CUDA-to-Ascend migration.

## The Layered API

CATLASS organizes a kernel into nested namespaces, each resolving one design dimension. Everything lives under `Catlass`.

### Arch — Target Hardware

`Arch::AtlasA2` selects the Atlas A2 (Ascend 910B) architecture, fixing the Cube/Vector instruction set and buffer geometry the lower layers compile against.

### Dispatch Policy — Pipeline Strategy

The dispatch policy chooses how the Cube pipeline is scheduled. `Gemm::MmadAtlasA2Pingpong<true>` selects a ping-pong (double-buffered) MMAD schedule that overlaps L1 loads with Cube compute. The boolean template argument toggles the pipelined variant.

### Tile Shapes — L1 and L0 Blocking

Two `GemmShape<M, N, K>` instantiations describe the two-level blocking that feeds the Cube unit:

- `L1TileShape = GemmShape<M, N, K>` — the block staged in the L1 buffer.
- `L0TileShape = GemmShape<M, N, K>` — the inner tile consumed from L0 by the Cube MMAD.

### GemmType — Operand Dtype and Layout

Each operand binds a dtype and a memory layout via `Gemm::GemmType<half, layout::RowMajor>`. Layouts come from the `layout` namespace (for example `layout::RowMajor`), making CATLASS layout-aware in the same way CUTLASS is — see wiki-nz-format for how row-major host data maps onto the NZ format the Cube unit expects.

### Block and Kernel — Assembling the Pieces

`Block::BlockMmad<Policy, L1TileShape, L0TileShape, AType, BType, CType>` composes the per-block matmul. `Kernel::BasicMatmul<Mmad, Epilogue, Scheduler>` wraps it into a launchable kernel, attaching an epilogue and a block scheduler.

### Scheduler — Block Swizzle

`GemmIdentityBlockSwizzle` maps the grid of output blocks onto AICores. The identity swizzle assigns blocks in natural order; alternative swizzles improve L2 locality for large problems.

## Putting It Together

The snippet below instantiates a basic FP16 matmul end to end. It follows the `00_basic_matmul` example on gitee Ascend/catlass.

```cpp
#include "catlass/gemm/gemm.hpp"

using namespace Catlass;

// 1. Architecture
using ArchTag = Arch::AtlasA2;

// 2. Dispatch policy: ping-pong (double-buffered) MMAD pipeline
using DispatchPolicy = Gemm::MmadAtlasA2Pingpong<true>;

// 3. Two-level tile shapes for L1 and L0
using L1TileShape = GemmShape<128, 256, 256>;
using L0TileShape = GemmShape<128, 256, 64>;

// 4. Operand dtypes + layouts
using AType = Gemm::GemmType<half, layout::RowMajor>;
using BType = Gemm::GemmType<half, layout::RowMajor>;
using CType = Gemm::GemmType<half, layout::RowMajor>;

// 5. Per-block matmul
using BlockMmad = Gemm::Block::BlockMmad<
    DispatchPolicy, L1TileShape, L0TileShape, AType, BType, CType>;

// 6. Block scheduler
using BlockScheduler = Gemm::Block::GemmIdentityBlockSwizzle<>;

// 7. Full kernel (Mmad, Epilogue=void, Scheduler)
using MatmulKernel = Gemm::Kernel::BasicMatmul<BlockMmad, void, BlockScheduler>;

// Launch on aicCoreNum AICores
MatmulKernel<<<aicCoreNum, nullptr, stream>>>(
    GemmCoord{M, N, K}, gmA, gmB, gmC);
```

`GemmCoord{M, N, K}` carries the problem size; `gmA`, `gmB`, `gmC` are device pointers to the operand and output tensors in Global Memory.

## Host Side — AscendCL Setup

The host program allocates device memory and stages operands with the AscendCL runtime, then launches the templated kernel on a stream. This is the same `aclrt*` flow used elsewhere in the knowledge base.

```cpp
// Allocate device buffers
aclrtMalloc(&gmA, sizeA, ACL_MEM_MALLOC_HUGE_FIRST);
aclrtMalloc(&gmB, sizeB, ACL_MEM_MALLOC_HUGE_FIRST);
aclrtMalloc(&gmC, sizeC, ACL_MEM_MALLOC_HUGE_FIRST);

// Stage inputs host -> device
aclrtMemcpy(gmA, sizeA, hostA, sizeA, ACL_MEMCPY_HOST_TO_DEVICE);
aclrtMemcpy(gmB, sizeB, hostB, sizeB, ACL_MEMCPY_HOST_TO_DEVICE);

// Launch
MatmulKernel<<<aicCoreNum, nullptr, stream>>>(
    GemmCoord{M, N, K}, gmA, gmB, gmC);
aclrtSynchronizeStream(stream);

// Copy result device -> host
aclrtMemcpy(hostC, sizeC, gmC, sizeC, ACL_MEMCPY_DEVICE_TO_HOST);
```

## Grouped GEMM for MoE

CATLASS extends beyond a single matmul. The `16_group_gemm` example batches many independent GEMMs of differing shapes into one launch — the access pattern behind Mixture-of-Experts (MoE) FFN layers, where each expert is a separate matmul over a variable token count. Instead of one launch per expert, a grouped kernel iterates a list of per-group `GemmCoord` problem sizes across the AICores, amortizing launch overhead. See kernel-grouped-gemm-ascendc for the hand-written counterpart and wiki-moe for the broader MoE context.

## Concept Mapping: CUTLASS to CATLASS

| CUTLASS concept | CATLASS counterpart | Role |
|-----------------|---------------------|------|
| `cutlass::arch::Sm90` | `Arch::AtlasA2` | Target architecture |
| Mainloop dispatch policy | `Gemm::MmadAtlasA2Pingpong<true>` | Pipeline schedule |
| `GemmShape<M,N,K>` (threadblock/warp) | `GemmShape<M,N,K>` (L1/L0) | Two-level tiling |
| `cutlass::half_t` + layout | `Gemm::GemmType<half, layout::RowMajor>` | Operand dtype + layout |
| Threadblock-level mainloop | `Block::BlockMmad<...>` | Per-block matmul |
| `cutlass::gemm::device::Gemm` | `Kernel::BasicMatmul<...>` | Launchable kernel |
| Threadblock swizzle | `GemmIdentityBlockSwizzle` | Block-to-core mapping |

## Trade-offs and Pitfalls

- **Tile shape must respect buffer geometry.** `L1TileShape` and `L0TileShape` are bounded by L1/L0 buffer capacity on Atlas A2; oversizing them fails to fit and a kernel that compiles may still be invalid for the target. Size tiles against the 910B buffer budget (see blog-ascend-910b-deep-dive) and keep dimensions aligned for the NZ format the Cube unit consumes.
- **Layout conversions are not free.** Declaring `layout::RowMajor` operands is convenient on the host, but Cube MMAD operates on NZ-formatted data. Conversions happen at boundaries; minimizing them is the same discipline described in blog-nz-format-explained.
- **The ping-pong policy assumes enough work to overlap.** `MmadAtlasA2Pingpong<true>` shines when L1 loads and Cube compute can genuinely overlap. For tiny or heavily memory-bound problems the double-buffering benefit shrinks — profile rather than assume.
- **Template error messages are dense.** As with CUTLASS, a single mismatched template parameter can produce a long instantiation trace. Start from a working example (`00_basic_matmul`) and change one parameter at a time.
- **Atlas A2 only.** The configurations described here target `Arch::AtlasA2` (Ascend 910B). Other Ascend parts are not covered by these dispatch policies.

## When to Use CATLASS

| Scenario | Recommendation |
|----------|----------------|
| Many GEMM shapes/dtypes to support | CATLASS — reuse one templated body |
| MoE / batched expert FFN | CATLASS grouped GEMM (`16_group_gemm`) |
| Migrating CUTLASS-based code to Ascend | CATLASS — concept-for-concept mapping |
| One fixed, hand-tuned fused kernel | Hand-written AscendC (kernel-matmul-ascendc) |

## Related Resources

- [Basic AscendC Matmul](kernel-matmul-ascendc) — hand-written counterpart
- [Grouped GEMM](kernel-grouped-gemm-ascendc) — MoE-style batched matmul
- [NZ Format Explained](blog-nz-format-explained) — the layout the Cube unit consumes
- [Ascend 910B Deep Dive](blog-ascend-910b-deep-dive) — Atlas A2 buffer and Cube geometry
