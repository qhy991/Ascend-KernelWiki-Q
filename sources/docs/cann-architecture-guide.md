---
id: doc-cann-architecture-guide
title: "CANN Architecture Guide — AICore Hardware Principles"
type: source-doc
architectures: [ascend910, ascend910b, ascend310p]
tags: [cann, architecture, aicore, hardware]
date: '2026-02-20'
url: https://www.hiascend.com/document/detail/en/canncommercial/800/opdevg/tbeaicpudevg/atlasopdev_10_0091.html
hardware_features: [cube-unit, vector-unit, scalar-unit, mte, unified-buffer, l1-buffer, global-memory, instruction-queue]
confidence: verified
---

The CANN Architecture Guide provides the foundational understanding of Ascend NPU hardware design and programming principles. At the core of each Ascend AI processor lies the AICore, a heterogeneous compute engine designed for deep learning workloads.

**AICore Internal Structure**: Each AICore contains three distinct execution units working in parallel:
- **Scalar Unit**: Handles control flow, address calculation, and lightweight arithmetic operations
- **Vector Unit**: Processes element-wise operations on 128-element vectors with high throughput
- **Cube Unit**: Dedicated matrix multiplication accelerator supporting mixed precision (FP16/BF16/INT8)

**Memory Hierarchy**: The architecture employs a tiered memory system optimized for data reuse:
- **Global Memory (GM)**: Large off-chip HBM storage
- **L1 Buffer**: On-chip intermediate cache with higher bandwidth
- **Unified Buffer (UB)**: Software-managed scratchpad for active data
- **L0 Buffer**: Register-file equivalent for immediate operand access

**Instruction Queue System**: AICore uses a queue-based execution model where operations are enqueued rather than executed immediately. This enables software pipelining and instruction-level parallelism through automatic scheduling by the hardware runtime.

**Operator Development Approaches**: The guide covers both TBE (Tensor Boost Engine) DSL and AscendC native programming paradigms, providing migration paths and compatibility considerations for existing operators.
