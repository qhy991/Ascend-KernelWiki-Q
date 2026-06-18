---
id: migration-aclnn-api
title: "aclnn (Single Operator API)"
type: wiki-migration
tags:
  - framework
confidence: inferred
sources: []
---

# aclnn (Single Operator API)

When migrating from CUDA, developers are accustomed to invoking `cuBLAS`, `cuDNN`, or directly launching `<<<grid, block>>>` kernels. On Ascend, the equivalent single-operator execution model is `aclnn` (Ascend C Language Neural Network API).

## Why aclnn?
Historically, Ascend execution heavily relied on Graph Engine (GE) compilation, meaning you had to build a full computational graph (`om` file) before running anything. This was highly hostile to dynamic frameworks like PyTorch eager mode.

The `aclnn` API was introduced to provide immediate, synchronous or asynchronous operator dispatch directly from the host.

## The Two-Step Execution Model
Every `aclnn` operator requires two steps:

1. **Workspace Calculation (`aclnn[OpName]GetWorkspaceSize`)**:
   Before running the operator, the host must ask the NPU how much temporary Global Memory (workspace) the operator needs.
   ```c
   uint64_t workspaceSize = 0;
   aclOpExecutor *executor = nullptr;
   aclnnAddGetWorkspaceSize(inputA, inputB, outputC, &workspaceSize, &executor);
   ```

2. **Operator Execution (`aclnn[OpName]`)**:
   Allocate the workspace (if > 0) and dispatch the operator to the specified ACL stream.
   ```c
   void *workspaceAddr = nullptr;
   if (workspaceSize > 0) {
       aclrtMalloc(&workspaceAddr, workspaceSize, ACL_MEM_MALLOC_HUGE_FIRST);
   }
   aclnnAdd(workspaceAddr, workspaceSize, executor, stream);
   ```

## Migration Equivalents
- `cublasSgemm` -> `aclnnMatmul`
- `cudnnConvolutionForward` -> `aclnnConvolution`
- `cudnnSoftmaxForward` -> `aclnnSoftmax`

## Integration with PyTorch
In `torch_npu`, every standard `aten::` operator is mapped to its corresponding `aclnn` call. The two-step workspace calculation is completely hidden within the PyTorch dispatcher.
