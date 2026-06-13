---
id: pattern-memory-bound
title: "Memory-Bound Kernel — Diagnosis and Resolution"
type: wiki-pattern
architectures: [ascend910, ascend910b]
tags: [memory-bound, diagnosis, performance, pattern]
confidence: inferred
sources: [blog-cann-training-camp, doc-ascend-memory-hierarchy]
symptoms: ["GM bandwidth >90% utilized", "Cube/Vector utilization <30%", "kernel time dominated by DataCopy", "low arithmetic intensity"]
techniques: [data-reuse, double-buffering, nz-tiling]
related: [technique-double-buffering, technique-data-reuse, hw-unified-buffer]
---

# Memory-Bound Kernel Pattern

## Problem

A memory-bound kernel spends most of its execution time waiting for data transfers between Global Memory (GM) and the Unified Buffer (UB), rather than performing actual computations. This is one of the most common performance bottlenecks in AscendC kernel development.

## Diagnostic Symptoms (via msprof)

Use `msprof` to identify memory-bound kernels by looking for:

- **GM bandwidth >90% utilized**: The kernel is saturating the available memory bandwidth
- **Cube/Vector utilization <30%**: Compute units are frequently idle waiting for data
- **Kernel time dominated by DataCopy operations**: Most time spent in `DataCopy()` calls rather than compute
- **Low arithmetic intensity**: Ratio of FLOPs to bytes transferred is low

## Root Causes

1. **Tiles too small**: Excessive GM transfers due to small tile sizes leading to high overhead relative to computation
2. **No double buffering**: Memory Transfer Engine (MTE) sits idle during compute phases instead of prefetching next tile
3. **No data reuse**: Same data loaded multiple times instead of being cached and reused in UB

## Solutions

### Increase Tile Size
Reduce the number of GM round-trips by processing larger tiles per iteration. Balance with UB capacity constraints.

### Implement Double Buffering
Use ping-pong buffers in UB: while one buffer is being processed by Cube/Vector, prefetch the next tile into the second buffer. This overlaps compute with memory transfer.

### Data Reuse
Cache data in UB across multiple operations. For example, in a fused operation, keep intermediate results in UB rather than writing back to GM and reloading.

## Diagnostic Flowchart

```
Check GM bandwidth in msprof
├─ >90% utilized → Likely memory-bound
│   ├─ Check tile size
│   │   └─ Too small? → Increase tile dimensions
│   ├─ Check pipeline overlap
│   │   └─ MTE idle during compute? → Add double buffering
│   └─ Check data access pattern
│       └─ Repeated loads of same data? → Implement data reuse
└─ ≤90% → Check compute utilization instead
```

## Related Patterns

- [Double Buffering Technique](/technique-double-buffering.md)
- [Data Reuse Pattern](/technique-data-reuse.md)
- [Unified Buffer Architecture](/hw-unified-buffer.md)
