---
id: pattern-low-cube-utilization
title: "Low Cube Utilization — Diagnosis and Resolution"
type: wiki-pattern
architectures: [ascend910, ascend910b]
tags: [cube-utilization, compute-bound, diagnosis, pattern]
confidence: inferred
sources: [blog-cann-training-camp, doc-catlass-framework]
symptoms: ["Cube utilization <50%", "Vector/MTE queues idle", "small matrix dimensions", "frequent Cube stalls"]
techniques: [nz-tiling, cube-vector-overlap, pipeline-scheduling]
related: [wiki-hardware-cube-unit, technique-cube-vector-overlap, technique-nz-tiling]
---

# Low Cube Utilization Pattern

## Problem

The Cube unit (matrix acceleration unit) is under-utilized, failing to achieve the theoretical FLOPS performance of the Ascend NPU. This leaves significant compute performance on the table.

## Diagnostic Symptoms (via msprof)

- **Cube utilization <50%**: Cube unit is frequently idle or not fully saturated
- **Vector queue idle between Cube operations**: Gaps in the pipeline where Vector has no work
- **Small matrix dimensions**: M, N, K dimensions too small to fill Cube tiles
- **Frequent Cube stalls**: Pipeline bubbles causing Cube to wait for data

## Root Causes

### 1. Small Matrix Dimensions
The Cube unit processes matrix tiles in NZ format. If input matrices (M, N, K) are small, the tiles don't fill the Cube's compute capacity, leading to poor utilization.

### 2. Sequential Cube→Vector Execution
Cube and Vector units have independent queues. Running them sequentially (wait for Cube to complete before starting Vector work) eliminates potential overlap and leaves one unit idle.

### 3. NZ Format Conversion Overhead
Cube operations require data in NZ format. If the kernel must frequently convert between standard and NZ formats, the conversion overhead can block Cube execution.

## Solutions

### Batch Small GEMMs
For small matrix dimensions, batch multiple independent GEMMs into a grouped GEMM operation. This allows the Cube to process larger aggregated tiles, improving utilization.

### Overlap Cube with Vector
Use independent queues to execute Cube and Vector operations concurrently. For example, while Cube computes matrix multiplication for iteration i, Vector can handle element-wise operations for iteration i-1.

### Pre-Convert to NZ Format
Convert input data to NZ format once at the kernel start, rather than converting on-the-fly within compute loops. Cache NZ-formatted data in UB for reuse.

## Implementation Pattern

```cpp
// Bad: Sequential execution
Matmul::Compute(tileA, tileB, tileC);  // Cube: wait for completion
Add::Compute(tileC, bias, tileC);       // Vector: starts after Cube

// Good: Overlapped execution
Matmul::Compute(tileA_i, tileB_i, tileC_i);   // Queue: Cube op i
Add::Compute(tileC_i-1, bias, tileC_i-1);     // Queue: Vector op i-1
// Cube i and Vector i-1 execute simultaneously
```

## Related Patterns

- [Cube Unit Architecture](/hw-cube-unit.md)
- [Cube-Vector Overlap Technique](/technique-cube-vector-overlap.md)
- [NZ Tiling Strategy](/technique-nz-tiling.md)
