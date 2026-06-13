---
id: blog-ascendc-performance-tips
title: "Top 10 AscendC Performance Optimization Tips"
type: source-blog
author: cann-developer
date: '2026-04-05'
url: https://www.hiascend.com/forum/thread-0292101.html
architectures: [ascend910, ascend910b]
tags: [optimization, performance, tips, ascendc]
techniques: [pipeline-scheduling, double-buffering, nz-tiling, cube-vector-overlap, data-reuse, bank-conflict-avoidance]
confidence: source-reported
---

# Top 10 AscendC Performance Optimization Tips

Practical performance optimization guide from CANN development team, distilled from real-world kernel tuning experience.

## 1. Maximize Tile Size Within UB Budget

**Tip**: Use largest possible tiles that fit in Unified Buffer to minimize Global Memory accesses.

**Impact**: 20-30% performance improvement from optimal tiling.

**Guideline**:
```ascendc
// Calculate UB budget
ub_budget = UB_total - workspace - output_buffer;

// Max tile for FP16 GEMM with double buffering
tile_size = ub_budget / (3 * sizeof(fp16));  // A, B, C buffers
tile_M = floor(sqrt(tile_size));
tile_N = tile_M;  // Square tiles usually optimal

// Pad to NZ alignment (16×)
tile_M = floor(tile_M / 16) * 16;
tile_N = floor(tile_N / 16) * 16;
```

**Avoid**: Tiny tiles (M,N < 64) that cause excessive GM round-trips.

## 2. Always Double-Buffer MTE Transfers

**Tip**: Overlap memory transfers with compute using double buffering.

**Impact**: 15-25% improvement for memory-bound kernels.

**Pattern**:
```ascendc
// Allocate two tile buffers
TBuf input_buf[2];
TBuf weight_buf[2];
int current = 0, next = 1;

// Initial load
DataCopy(input_buf[0], gm_input, tile_size);
DataCopy(weight_buf[0], gm_weight, tile_size);
PipeBarrier();

// Loop with overlap
for (int t = 1; t < num_tiles; t++) {
    // Load next tile (async)
    DataCopy(input_buf[next], gm_input[t], tile_size);
    DataCopy(weight_buf[next], gm_weight[t], tile_size);
    
    // Compute current tile
    Matmul(input_buf[current], weight_buf[current], output[t-1]);
    
    // Swap buffers
    current = (current + 1) % 2;
    next = (next + 1) % 2;
}
```

## 3. Overlap Cube and Vector via Independent Queues

**Tip**: Use separate queues for Cube (matmul) and Vector (epilogue) operations.

**Impact**: 10-20% improvement for kernels with complex epilogues.

**Example**:
```ascendc
// Enqueue operations independently
QueueEnqueue(CUBE_QUEUE, matmul_op);
QueueEnqueue(VECTOR_QUEUE, bias_add_op);
QueueEnqueue(VECTOR_QUEUE, activation_op);
// CUBE and VECTOR execute concurrently
```

## 4. Keep Data in NZ Format Throughout Pipeline

**Tip**: Minimize format conversions; stay in NZ format internally.

**Impact**: 10-15% reduction in conversion overhead.

**Pattern**:
```ascendc
// Convert at boundaries only
DataCopy(gm_input, nz_input, size, ND_TO_NZ);  // Once at start

// All operations in NZ
Matmul(nz_input, nz_weight, nz_output);
Add(nz_output, nz_bias, nz_output);
GELU(nz_output, nz_output);

// Convert back at end
DataCopy(nz_output, gm_output, size, NZ_TO_ND);  // Once at end
```

## 5. Minimize PipeBarrier Calls

**Tip**: Only insert `PipeBarrier()` when data dependency requires synchronization.

**Impact**: 5-10% improvement from reduced serialization.

**Anti-pattern**:
```ascendc
// BAD: Barrier after every operation
DataCopy(A_ub, A_gm, size);
PipeBarrier();  // Unnecessary
Matmul(A_ub, B_ub, C_ub);
PipeBarrier();  // Unnecessary
ReLU(C_ub, C_ub);
```

**Correct**:
```ascendc
// GOOD: Only barrier before dependency
DataCopy(A_ub, A_gm, size);
DataCopy(B_ub, B_gm, size);
Matmul(A_ub, B_ub, C_ub);  // Automatically waits for DataCopy
PipeBarrier();  // Only before final store
DataCopy(C_gm, C_ub, size);
```

## 6. Reuse UB Data Across Multiple Operations

**Tip**: Keep hot data in UB rather than reloading from GM.

**Impact**: 15-20% improvement for weight-heavy operations.

**Example**:
```ascendc
// Load weights once, reuse for multiple matmuls
DataCopy(gm_weights, ub_weights, K*N);  // Load once

for (int b = 0; b < batch_size; b++) {
    DataCopy(ub_input[b], gm_input[b], M*K);
    Matmul(ub_input[b], ub_weights, ub_output[b]);  // Reuse weights
    // ... epilogue operations
}
```

## 7. Pad Dimensions to Avoid Bank Conflicts

**Tip**: Pad matrix dimensions to avoid UB bank conflicts.

**Impact**: 5-10% improvement from better memory bandwidth utilization.

**Guideline**: For FP16, pad leading dimensions to multiples of 64.

## 8. Use L1 Buffer for Frequently Accessed Weights

**Tip**: Cache weights in L1 (between GM and UB) for repeated access.

**Impact**: 10-15% improvement for convolution/small-GEMM workloads.

**API**: Use `L1Buffer` allocation with `DataCopy` from GM to L1, then L1 to UB.

## 9. Batch Small Ops into Grouped Kernels

**Tip**: Combine many small operations into grouped kernel to reduce launch overhead.

**Impact**: 20-30% improvement for many-small-op workloads (e.g., per-token MLPs).

**Pattern**: Use [Grouped GEMM](kernel-grouped-gemm-ascendc) instead of individual matmul launches.

## 10. Profile with msprof Before and After Each Optimization

**Tip**: Measure actual performance impact; don't assume optimizations help.

**Tool**: `msprof` application timeline and queue analysis.

**Metric**: Track AICore utilization, queue idle time, GM bandwidth.

## Optimization Priority

Start with high-impact, low-effort optimizations:
1. Tiling (Tip 1)
2. Double buffering (Tip 2)
3. Minimize barriers (Tip 5)
4. NZ format (Tip 4)

Then move to advanced optimizations once foundation is solid.

## Common Pitfalls

- **Over-tiling**: Too-large tiles exceed UB capacity → runtime error
- **Over-optimizing**: Spending effort on <5% improvements
- **Ignoring hardware**: 910A optimizations may not transfer to 910B

## Related Patterns

- [Pipeline Scheduling](technique-pipeline-scheduling) — comprehensive queue overlap
- [Double Buffering](technique-double-buffering) — MTE/compute overlap
- [NZ Tiling](technique-nz-tiling) — format-aware tile sizing
