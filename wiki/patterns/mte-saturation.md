---
id: pattern-mte-saturation
title: "MTE Saturation (Bandwidth Bound)"
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

# MTE Saturation (Bandwidth Bound)

Memory Transfer Engine (MTE) saturation occurs when the AI Core spends the majority of its time waiting for data to arrive from Global Memory (GM) into the Unified Buffer (UB), while the Cube and Vector units sit idle.

## Symptoms
When using the `msprof` tool:
- **Task Timeline**: Large gaps between Vector/Cube blocks.
- **AI Core Metrics**: `MacRatio` (Cube utilization) and `VecRatio` are very low (< 20%). `Mte1Ratio` or `Mte2Ratio` are exceptionally high (> 80%).

## Diagnosis & Solutions

### 1. Small Contiguous Reads
The MTE relies on bursting wide, contiguous blocks from HBM. If your `DataCopy` instructions request very small chunks (e.g., 16 bytes at a time) or use scattered strides, the memory controller efficiency plummets.
- **Fix**: Increase the tile size (`blockDim` / UB capacity planning) so that each `DataCopy` moves at least several kilobytes contiguously.

### 2. High 3D Cube Dimensions
If you are mapping tensors directly to L1/L0A using `DataCopyExtParams` and the data is highly fragmented (e.g., reading a column of a row-major matrix), MTE performance degrades.
- **Fix**: Use `Nd2Nz` (N-dimensional to Fractal-Z) format conversions. Restructure your tensors in Global Memory so the hardware can read them natively in the format the Cube unit expects (16x16 blocks).

### 3. Missing Double-Buffering
If the MTE and Compute pipelines are serialized, MTE will appear as the bottleneck because Compute cannot overlap it.
- **Fix**: Implement `TQue` with a depth of 2 or more to enable Ping-Pong overlapping.

### 4. Arithmetic Intensity
If the kernel inherently does very little math per byte loaded (e.g., Element-wise Add, LayerNorm), it is mathematically impossible to hide the memory latency. 
- **Fix**: Apply **Operator Fusion**. Fuse this operation into the preceding or succeeding layer to avoid the GM roundtrip entirely.
