---
id: blog-ascendc-programming-guide
title: "Notes on Ascend C Operator Development — Comparative Study with CUDA"
type: source-blog
author: xiaodouzi6661
date: '2025-08-15'
url: https://medium.com/@xiaodouzi6661/notes-on-the-basic-stage-of-cann-training-camp-ascend-c-operator-development-comparative-study-0f3050406380
architectures: [ascend910, ascend910b]
tags: [ascendc, programming, cuda-comparison, tutorial]
techniques: [pipeline-scheduling]
languages: [ascendc]
confidence: source-reported
---

This blog post provides a practical introduction to AscendC operator development through comparative analysis with CUDA programming model. The author, drawing from CANN Training Camp experience, highlights key architectural differences and practical migration considerations.

**Programming Model Comparison**:
- **Thread Model**: AscendC uses implicit parallelism through queue-based execution, contrasting with CUDA's explicit thread hierarchy (grid/block/thread)
- **Memory Management**: AscendC requires explicit staging through Unified Buffer with allocation/deallocation, while CUDA uses shared memory with thread-group synchronization
- **Synchronization**: AscendC employs pipe-based async primitives, CUDA uses barriers and __syncthreads()

**Pipeline Architecture**: The CopyIn→Compute→CopyOut pattern is central to AscendC:
1. **CopyIn Stage**: Move input data from GM to UB using DataCopy API
2. **Compute Stage**: Execute Vector/Cube operations on UB-resident data
3. **CopyOut Stage**: Write results back to GM with appropriate synchronization

**Queue-Based Tensor Management**: Unlike CUDA's immediate execution model, AscendC operations are enqueued:
- Operations accumulate in instruction queues
- Explicit progression calls trigger execution
- Enables software pipelining and compiler optimization
- Requires careful dependency management

**Key Differences from CUDA**:
- No thread indexing constructs (blockIdx/threadIdx) — loop-based parallelism
- Fixed execution units (Vector/Cube) rather than programmable SMs
- Explicit memory hierarchy management vs. automatic cache hierarchy
- Queue-based execution vs. immediate kernel launches

The post includes code examples comparing equivalent implementations in both frameworks and provides practical tips for CUDA programmers transitioning to AscendC development.
