---
id: wiki-pattern-tque-deadlock
title: TQue Deadlock Pattern in Ascend C
type: wiki-pattern
architectures: [ascend910, ascend910b]
tags: [instruction-queue, pipeline-scheduling, ascendc]
confidence: verified
sources: [doc-ascendc-api-reference]
---

# TQue Deadlock

Queue deadlocks are one of the most common issues when writing Ascend C pipeline kernels. They occur when the pipeline stalls permanently due to an improper sequence of `AllocTensor`, `EnQue`, `DeQue`, and `FreeTensor`.

## Symptoms

- Kernel hangs indefinitely.
- `msprof` shows no computation after a certain point.
- Only a few tiles process before execution completely stops.

## Common Causes

### 1. Missing FreeTensor
If a `LocalTensor` is `DeQue`'d but never returned to the pool using `FreeTensor`, the pool of available buffers is exhausted.

```cpp
// BAD
LocalTensor<half> xLocal = inQueue.DeQue<half>();
// ... compute ...
// Missing: inQueue.FreeTensor(xLocal);

// GOOD
LocalTensor<half> xLocal = inQueue.DeQue<half>();
// ... compute ...
inQueue.FreeTensor(xLocal); 
```

### 2. Mismatched Alloc/EnQue
Calling `AllocTensor` but forgetting to `EnQue` means the downstream component will hang indefinitely on its `DeQue` call.

```cpp
// BAD
LocalTensor<half> xLocal = outQueue.AllocTensor<half>();
// ... write data ...
// Missing: outQueue.EnQue(xLocal);
```

### 3. Loop Iteration Count Mismatch
If the producer (`CopyIn`) loops `N` times but the consumer (`Compute`) loops `M` times, one will wait on a queue forever.

## Solution and Best Practices

- Always ensure that for every `AllocTensor`, there is a corresponding `EnQue` or `FreeTensor`.
- Always ensure that for every `DeQue`, there is a corresponding `FreeTensor` or `EnQue`.
- Keep loop boundaries synchronized between pipeline stages.
- When branching, ensure tensors are freed or enqueued along all control paths.
