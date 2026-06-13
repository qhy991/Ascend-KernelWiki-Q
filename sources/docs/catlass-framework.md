---
id: doc-catlass-framework
title: "Catlass — Modular GEMM Framework for Ascend (CUTLASS equivalent)"
type: source-doc
architectures: [ascend910, ascend910b]
tags: [catlass, gemm, matmul, library]
date: '2025-12-15'
url: https://www.hiascend.com/document/detail/en/canncommercial/800/opdevg/Ascendcopdevg/atlas_ascendc_10_0060.html
hardware_features: [cube-unit, unified-buffer]
techniques: [pipeline-scheduling, double-buffering, nz-tiling]
confidence: verified
---

Catlass is Ascend's modular GEMM framework, providing a composable abstraction for building high-performance matrix multiplication kernels analogous to NVIDIA's CUTLASS library. The framework decomposes GEMM implementation into three logical stages that can be independently configured and optimized.

**Framework Architecture**:
- **Prologue**: Input data preparation including format conversion (ND→NZ), padding, and transformation
- **Mainloop**: Tiled matrix multiplication with hierarchical blocking and software pipelining
- **Epilogue**: Output processing including bias addition, activation functions, and format conversion (NZ→ND)

**Template-Based Tiling**: Catlass uses C++ templates to generate specialized kernels for different:
- Block sizes (16×16, 32×32, 64×64) matching Cube unit requirements
- Data types (FP16, BF16, INT8) with automatic precision promotion handling
- Memory layouts supporting various input format combinations

**NZ Format Integration**: Native support for FRACTAL_NZ format throughout the pipeline:
- Automatic tile size calculation based on Cube unit constraints
- Efficient address generation for 5D indexed access patterns
- Conversion optimization in prologue/epilogue stages

**Performance Features**:
- Pipeline scheduling with configurable stage depths
- Double buffering for hiding memory latency
- Vector-Cube operation overlap for maximum utilization
- Bank conflict avoidance through intelligent tile partitioning

The framework provides reference implementations for common GEMM variants and supports custom kernel development through modular component extension.
