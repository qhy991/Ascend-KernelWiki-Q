---
id: technique-async-dma-multistage
title: "Asynchronous DMA & Multi-stage Pipelines"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - performance
confidence: inferred
sources: []
---

# Asynchronous DMA & Multi-stage Pipelines

To hide memory latency, Ascend NPU programming heavily relies on overlapping Data DMA (Direct Memory Access) with computation. The Memory Transfer Engine (MTE) handles asynchronous copies between Global Memory (GM) and on-chip buffers (L1, UB, L0).

## Double Buffering (Ping-Pong)
The simplest pipeline is a 2-stage double buffer:
1. **Buffer 0**: MTE loads tile `i` from GM to UB.
2. **Buffer 1**: Vector unit computes on tile `i-1`.
When both complete, they swap roles. This hides the MTE latency entirely if `T_compute >= T_load`.

## Triple and Multi-Stage Buffering
In complex operators (like Attention), double buffering may not be enough to hide latency, especially if there are significant pipeline bubbles between the Vector and Cube units. 

A Triple Buffer (or N-stage pipeline) allocates 3 or more blocks in the `TQue`.
```cpp
// Allocate a queue with depth 3
TQue<QuePosition::VECIN, 3> inQueue;
```
This allows the MTE to fetch tile `i+1` and `i+2` ahead of time while the Compute units are still struggling with tile `i`. Multi-stage buffering requires more Unified Buffer (UB) capacity, meaning your tile size (`blockDim` / `TilingData`) must shrink to fit $N$ buffers simultaneously.

## Implementing with AscendC TPipe
The `TPipe` and `TQue` APIs natively manage the asynchronous DMA. 
```cpp
// 1. Allocate block
LocalTensor<half> local_tensor = inQueue.AllocTensor<half>();

// 2. Issue Async DMA (DataCopy)
DataCopy(local_tensor, global_tensor, size);

// 3. Enqueue to signify DMA completion to the compute unit
inQueue.EnQue(local_tensor);
```
The `DataCopy` call returns immediately to the host CPU, allowing the next instructions to issue, but the `EnQue` blocks until the DMA hardware flag signals completion.
