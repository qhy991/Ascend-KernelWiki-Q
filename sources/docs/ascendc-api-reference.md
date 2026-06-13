---
id: doc-ascendc-api-reference
title: "AscendC API Reference (CANN 8.0)"
type: source-doc
architectures: [ascend910, ascend910b, ascend310p]
tags: [ascendc, api, operator, cann]
date: '2026-03-15'
url: https://www.hiascend.com/document/detail/en/canncommercial/800/opdevg/Ascendcopdevg/atlas_ascendc_10_0056.html
hardware_features: [cube-unit, vector-unit, unified-buffer, mte]
confidence: verified
---

The official AscendC API reference provides comprehensive documentation for developing high-performance operators on Ascend NPUs. The API is organized into four primary categories that map directly to the AICore hardware architecture:

**Vector API**: Provides element-wise operations on the Vector unit, including arithmetic, logical, and mathematical functions. Supports in-place computation with automatic allocation strategies and provides optimized primitives for common vector operations like activation functions and normalization.

**Cube API**: Dedicated matrix multiplication interface for the Cube unit, supporting FP16/BF16/INT8 data types. Includes specialized APIs for GEMM operations with configurable precision and supports batched matrix multiplication with efficient tensor core utilization.

**DataCopy/MTE API**: Manages data movement between memory hierarchy levels using the Memory Transfer Engine. Provides efficient GM↔UB transfers, supports overlapping computation with data movement through double buffering, and enables zero-copy operations within the Unified Buffer.

**Synchronization Primitives**: Includes pipe-based synchronization for multi-core coordination, local and global event management for pipeline staging, and barrier operations for thread-level synchronization.

The reference includes detailed parameter descriptions, performance guidelines, and code examples for common operator patterns.
