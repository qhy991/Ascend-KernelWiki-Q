---
id: doc-ascend-memory-hierarchy
title: "Ascend Memory Hierarchy and Data Movement"
type: source-doc
architectures: [ascend910, ascend910b]
tags: [memory, unified-buffer, global-memory, data-movement]
date: '2026-01-10'
url: https://www.hiascend.com/document/detail/en/canncommercial/800/opdevg/Ascendcopdevg/atlas_ascendc_10_0038.html
hardware_features: [global-memory, l1-buffer, unified-buffer, l0-buffer, mte]
techniques: [data-reuse, double-buffering]
confidence: verified
---

The Ascend memory architecture implements a 4-level hierarchy designed to maximize data reuse and minimize latency for compute-intensive workloads. Understanding data movement patterns is critical for achieving peak performance on Ascend NPUs.

**Memory Hierarchy Levels**:
- **Global Memory (GM)**: High-capacity HBM with ~1.2 TB/s bandwidth on Ascend910B
- **L1 Buffer**: On-chip cache with software-managed allocation for intermediate data
- **Unified Buffer (UB)**: 256KB software-controlled scratchpad per AICore for active working sets
- **L0 Buffer**: Register file for immediate computation operands

**DataCopy API**: The primary interface for GM↔UB data movement, providing:
- Explicit transfer control with asynchronous execution capability
- Support for strided access patterns and tensor slicing operations
- Integration with the MTE (Memory Transfer Engine) for efficient DMA operations
- Automatic bank conflict avoidance through intelligent address allocation

**L1 Buffer Management**: Serves as a staging area between GM and UB, particularly useful for:
- Intermediate storage in multi-pass algorithms
- Reducing GM traffic through data reuse
- Enabling software-managed cache policies for specific access patterns

**UB Allocation Strategies**: Critical considerations for maximizing performance:
- Bank-aware allocation to prevent conflicts (32 banks with modulo addressing)
- Double buffering to overlap computation with data movement
- Lifetime management through explicit allocation/deallocation calls
- Static allocation for compile-time determinism where possible

The guide provides bandwidth characteristics, latency estimates, and optimization checklists for common data movement patterns.
