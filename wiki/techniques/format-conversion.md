---
id: technique-format-conversion
title: "ND ↔ NZ Format Conversion Optimization"
type: wiki-technique
architectures: [ascend910, ascend910b]
tags: [format-conversion, nz-format, nd-format, optimization]
confidence: source-reported
techniques: [format-conversion]
hardware_features: [nz-format, nd-format, vector-unit]
kernel_types: [gemm, attention]
related: [hw-cube-unit, technique-nz-tiling]
sources: [blog-nz-format-explained, doc-cann-architecture-guide]
reproducibility: snippet
---

# ND ↔ NZ Format Conversion Optimization

The Ascend Cube unit requires tensors in FRACTAL_NZ format (5D: N, Z, C, H, W) for efficient computation, but most input data follows conventional ND (row-major) format. This format mismatch necessitates conversion operations that impact performance.

## Conversion Overhead

Format conversion between ND and NZ formats imposes several costs:

- **Vector unit operations**: Conversion requires vector instructions to rearrange data layout
- **UB space allocation**: Additional Unified Buffer capacity needed for intermediate results
- **Pipeline stalls**: Synchronization between Vector and Cube units during conversion

Performance measurements indicate naive conversion can consume 5-15% of total kernel execution time in compute-bound operations.

## Optimization Strategies

### 1. Persistent NZ Format
Maintain data in NZ format throughout the entire pipeline to eliminate repeated conversions. This strategy works best when multiple operations can be chained without GM access.

### 2. Vector Unit Conversion
Leverage the Vector unit for efficient format conversion using the `DataCopyPad` API:

```cpp
// AscendC example: ND to NZ conversion
DataCopyPad(dst_nz_tensor, src_nd_tensor, pad_mode);
```

This approach performs conversion and padding in a single operation, minimizing UB footprint.

### 3. Fused CopyIn Stage
Integrate conversion with the initial CopyIn from Global Memory to UB, reducing explicit conversion stages.

## Impact Analysis

The choice of conversion strategy significantly affects overall kernel performance:

- **Naïve per-tile conversion**: 10-15% overhead, suitable for low-tile-count operations
- **Persistent NZ format**: 5-8% overhead initially, but amortized across multiple operations
- **Fused CopyIn conversion**: Minimal overhead (<5%) when carefully integrated with pipeline scheduling

For GEMM kernels with high tile reuse, persistent NZ format with one-time conversion typically yields optimal results.