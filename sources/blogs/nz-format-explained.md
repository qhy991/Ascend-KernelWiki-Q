---
id: blog-nz-format-explained
title: "Understanding FRACTAL_NZ — Ascend's 5D Data Format for Matrix Computation"
type: source-blog
author: ascend-developer
date: '2025-11-20'
url: https://www.hiascend.com/forum/thread-0285101.html
architectures: [ascend910, ascend910b]
tags: [nz-format, data-format, cube-unit, matrix]
hardware_features: [nz-format, cube-unit]
techniques: [nz-tiling, format-conversion]
confidence: source-reported
---

FRACTAL_NZ (commonly called NZ format) is Ascend's proprietary 5D tiled data layout required by the Cube matrix unit for efficient matrix multiplication. This post explains the format's structure, rationale, and practical considerations for operator developers.

**5D Dimension Structure**: The NZ format uses five indices (C1, H, C0, Ni, No) to represent a tiled matrix:
- **C1**: Number of complete tiles in the C dimension (tile row count)
- **H**: Height/row dimension within a tile
- **C0**: Fixed block size (typically 16) representing the tile's C0 dimension
- **Ni**: Inner dimension for matrix multiplication tiling
- **No**: Outer dimension for matrix multiplication tiling

**Tiling Requirements**:
- C0 must be 16 for FP16/BF16 matrices to match Cube unit requirements
- Total size must be padded to 16×16 block boundaries
- Tiles are arranged in row-major order for efficient spatial locality
- Memory addresses follow a specific 5D stride pattern

**Format Conversion Costs**:
- **ND→NZ Conversion**: Required before Cube unit computation, adds latency
- **NZ→ND Conversion**: Required for output compatibility, non-trivial overhead
- **In-NZ Computation**: Chaining multiple NZ operations avoids conversion costs
- **NZ-aware Operators**: Design operators to work natively in NZ format

**Practical Considerations**:
- Conversion overhead can be amortized across multiple operations
- Memory layout affects bank conflicts — careful tile sizing required
- Not all operators benefit from NZ format — Vector operations often prefer NCHW
- Automatic conversion helpers provided in AscendC API but optimization requires manual tuning

**Performance Impact**:
- Proper NZ formatting enables near-peak Cube unit utilization (up to 256 TFLOPS)
- Incorrect tiling can lead to 50%+ performance degradation
- Bank conflicts from poor tile distribution cause additional throughput loss

The post includes visual diagrams of the 5D layout, conversion code examples, and performance benchmarks comparing NZ-aware vs. naive implementations.
