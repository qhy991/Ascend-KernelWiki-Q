---
id: technique-pr-catlass-218
title: "PR Insight: ascend/catlass #218"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - performance
  - optimization
  - kernel
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/218"
---

# PR Insight: ascend/catlass #218 - 新增 31_small_matmul 算子

## Overview
This pull request introduces a new optimized operator example, `31_small_matmul`, into the ascend/catlass repository. The PR specifically focuses on optimizing General Matrix Multiplication (GEMM) for **small shape scenarios** by stripping out unnecessary scalar calculation overhead typically found in the `basic_matmul` implementation. 

## Architectural & Technical Insights

When executing GEMM operations on small matrices, the overhead of scalar operations (such as loop condition checks, address calculations, and synchronization) can constitute a significant portion of the total execution time, leading to suboptimal performance on the Ascend NPUs. 

The `31_small_matmul` example solves this by utilizing the specialized `Gemm::MmadAtlasA2Small` dispatch policy under the `AtlasA2` architecture:

```cpp
using DispatchPolicy = Gemm::MmadAtlasA2Small<STAGES, ENABLE_UNIT_FLAG, ENABLE_SHUFFLE_K>;
using L1TileShape = GemmShape<128, 256, 256>;
using L0TileShape = GemmShape<128, 256, 64>;
```

### Constraints and Optimizations

Because this kernel aggressively optimizes away generic loops and shape checks, it imposes strict constraints on the input matrix sizes to guarantee that the workload fits seamlessly within the hardware limits without needing complex blocking or iterative tiling across the K dimension.

1. **Tile Block Count Limitation**: 
   The total number of required tile blocks must not exceed the available Cube cores (`aicCoreNum`) on the device. This ensures the entire computation can be dispatched in a single wave, completely avoiding the overhead of block scheduling across multiple waves.
   `ceilDiv(M, L1TileShape::M) * ceilDiv(N, L1TileShape::N) <= aicCoreNum`

2. **K-Dimension Limitation**:
   The `K` dimension of the matrix must be less than or equal to `L1TileShape::K` (e.g., 256). This restricts the kernel to loading the entire K dimension into the L1 buffer without needing to chunk the operation along the K axis, thereby eliminating the K-loop overhead and ensuring a single accumulation phase.

## Usage

The kernel is executed directly via `SmallMatmul<<<aicCoreNum, nullptr, stream>>>(...)`. This mapping leverages a direct hardware parallelization model using `aicCoreNum`, optimizing occupancy for workloads that meet the constraints.

If the dimensions of the matrix exceed these constraints, users are advised to fall back to `09_splitk_matmul` or the generic `06_optimized_matmul`.

## Conclusion
This optimization represents a critical technique in hardware architecture specific to Ascend NPUs: trading off generality for performance in specialized small-shape AI inference cases (e.g., small MLPs or attention heads). By guaranteeing single-wave dispatch and single-pass accumulation, the `31_small_matmul` drastically reduces scalar overhead and maximizes tensor core utilization.
