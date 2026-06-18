---
id: pattern-scalar-bottleneck
title: "Scalar Unit Bottlenecks"
type: wiki-pattern
architectures:
  - ascend910
  - ascend910b
tags:
  - debugging
  - performance
confidence: inferred
sources: []
---

# Scalar Unit Bottlenecks

The Scalar Unit on the Ascend AI Core is primarily responsible for address calculations, loop control, and branch resolution. While the Cube and Vector units provide massive TFLOPS, they can be starved if the Scalar Unit cannot issue instructions fast enough.

## Symptoms
- In `msprof`, the `ScalarRatio` is disproportionately high, while `VecRatio` and `MacRatio` are low.
- "Instruction Queue Empty" events are frequent, indicating the Compute units are waiting for the Scalar unit to tell them where to read/write memory.

## Causes and Fixes

### 1. Complex Address Arithmetic
If your kernel uses multi-dimensional, non-contiguous indexing with complex modulo (`%`) and division (`/`) operations inside the inner loops to calculate UB offsets, the Scalar Unit will choke.
- **Fix**: Pre-calculate strides outside the loop. Use AscendC's native `DataCopy` with `DataCopyExtParams` to let the hardware handle multidimensional strides automatically, rather than computing linear indices manually in the Scalar unit.

### 2. Excessive Loop Unrolling/Overhead
Writing loops that process 1 or 2 elements at a time forces the Scalar unit to execute branching instructions constantly.
- **Fix**: Vectorize! The Vector unit works on blocks of 256 bytes (e.g., 128 `fp16` elements) per instruction. Ensure your inner loops are processing data in chunks of at least 256 bytes, allowing the Scalar unit to step by large increments.

### 3. Conditional Branches (Divergence)
`if/else` statements inside the innermost loop cause branch prediction misses and scalar stalls.
- **Fix**: Use Vector unit masking (`SetMask`) or `Select` (Predication) instructions. Compute both branches in the Vector unit and use a hardware mask to merge the results, entirely bypassing the Scalar branch instruction.
