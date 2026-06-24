---
id: pattern-pipeline-stall
title: "Pipeline Stall — Queue Dependency Bottleneck"
type: wiki-pattern
architectures: [ascend910, ascend910b]
tags: [pipeline, stall, queue, dependency, diagnosis, pattern]
confidence: inferred
sources: [blog-cann-training-camp, doc-cann-architecture-guide]
symptoms: ["MTE queue idle while Vector waits", "Cube queue has gaps between operations", "PipeBarrier taking >10% of kernel time", "Low overall AICore utilization"]
techniques: [pipeline-scheduling, double-buffering, cube-vector-overlap]
related: [wiki-hardware-instruction-queue, technique-pipeline-scheduling, technique-double-buffering]
---

# Pipeline Stall Pattern

Pipeline stalls occur when one instruction queue waits for another queue to complete, creating idle time and reducing AICore utilization. Ascend's three-queue architecture (MTE, Vector, Cube) is designed for concurrent execution, but incorrect synchronization can serialize operations.

## Three Queue Architecture

- **MTE Queue**: Memory transfer operations (DataCopy)
- **Vector Queue**: Element-wise operations (arithmetic, activation, format conversion)
- **Cube Queue**: Matrix multiplication operations

When properly overlapped, all three queues execute concurrently. When stalled, one queue sits idle while another works.

## Common Causes

### 1. Excessive PipeBarrier Calls

**Problem**: Calling `PipeBarrier()` after every operation forces serialization.

**Symptom**: Low AICore utilization (~30-40%), timeline shows sequential execution.

**Solution**: Only synchronize when data dependency is unavoidable:
```ascendc
// BAD: Barrier after every operation
DataCopy(A_ub, A_gm, size);
PipeBarrier();
Matmul(A_ub, B_ub, C_ub, M, N, K);
PipeBarrier();
ReLU(C_ub, C_ub, size);

// GOOD: Only barrier before dependency
DataCopy(A_ub, A_gm, size);
DataCopy(B_ub, B_gm, size);
Matmul(A_ub, B_ub, C_ub, M, N, K);  // Waits for DataCopy automatically
PipeBarrier();  // Only before ReLU that depends on Matmul
ReLU(C_ub, C_ub, size);
```

### 2. MTE Bottleneck

**Problem**: DataCopy can't feed compute fast enough.

**Symptom**: MTE queue at 100%, Vector/Cube queues have gaps.

**Solution**: Use [Double Buffering](technique-double-buffering) to overlap MTE with compute:
- Load next tile while computing current tile
- Ensures compute queue never starves for data

### 3. UB Pressure

**Problem**: Not enough Unified Buffer space for multiple tiles, preventing double buffering.

**Symptom**: Can't allocate second tile, forced to sequential load-compute-store.

**Solution**: Reduce per-tile size to allow two tiles in UB:
```ascendc
// Smaller tiles enable double buffering
tile_M = 128;  // Instead of 256
tile_N = 256;  // Instead of 512
// Now UB fits: tile_current + tile_next + output
```

## Diagnostics with msprof

**Queue Timeline**: Look for gaps between operations in same queue.

**Barrier Percentage**: If `PipeBarrier` or related synchronization takes >10% of kernel time, investigate barrier placement.

**Utilization by Queue**: Healthy pipelines show all queues at >80% utilization concurrently.

## Solutions Priority

1. **Remove unnecessary barriers** — 5-10% improvement typical
2. **Add double buffering** — 15-25% improvement if MTE-bound
3. **Reduce tile size** — enables double buffering, costs 5-10% in tiling overhead
4. **Event-based sync** — instead of full barrier, use `Event` API for finer-grained dependencies

## Example: Event-Based Synchronization

```ascendc
Event load_done, compute_done;

// MTE queue
DataCopy(A_ub, A_gm, size);
RecordEvent(load_done);

// Vector queue — wait only for specific event
WaitEvent(load_done);
Matmul(A_ub, B_ub, C_ub, M, N, K);
RecordEvent(compute_done);

// Next operation
WaitEvent(compute_done);
```

## Related Patterns

- [Pipeline Scheduling](technique-pipeline-scheduling) — comprehensive overlap strategies
- [Double Buffering](technique-double-buffering) — MTE/compute overlap implementation
- [Instruction Queue](hw-instruction-queue) — hardware architecture details
