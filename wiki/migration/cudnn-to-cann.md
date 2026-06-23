---
id: migration-cudnn-to-cann
title: "cuDNN to CANN (aclnn) Migration Guide"
type: wiki-migration
architectures: [ascend910, ascend910b]
tags: [migration]
confidence: verified
sources: []
---

# cuDNN to CANN Migration Guide

When migrating deep learning models from NVIDIA to Huawei Ascend NPUs, the functionality of cuDNN is replaced by the CANN (Compute Architecture for Neural Networks) NN operator library, specifically the `aclnn` API.

## Conceptual Differences

- **cuDNN**: A stateful C API where you create descriptors (`cudnnTensorDescriptor_t`), set their properties, and pass them to execution functions.
- **aclnn**: CANN's modern NN API is stateless and divided into a two-step process: **Workspace Size Calculation** and **Execution**.

## The `aclnn` Two-Step Paradigm

Unlike cuDNN's descriptor-heavy approach, `aclnn` functions generally follow this pattern:

### 1. Get Workspace Size
You call the `GetWorkspaceSize` variant of the operator to determine how much temporary memory the NPU requires.
```cpp
uint64_t workspaceSize = 0;
aclOpExecutor* executor = nullptr;
// Example: Calculate workspace for ReLU
aclnnReluGetWorkspaceSize(inputTensor, outputTensor, &workspaceSize, &executor);
```

### 2. Execute
Allocate the workspace, then pass the executor and workspace to the NPU stream.
```cpp
void* workspaceAddr = nullptr;
aclrtMalloc(&workspaceAddr, workspaceSize, ACL_MEM_MALLOC_HUGE_FIRST);

// Execute the operator asynchronously on the stream
aclnnRelu(workspaceAddr, workspaceSize, executor, stream);
```

## Key API Mapping

| NVIDIA cuDNN | Ascend CANN `aclnn` |
|--------------|---------------------|
| `cudnnConvolutionForward()` | `aclnnConvolution()` |
| `cudnnActivationForward()` | `aclnnRelu()`, `aclnnGelu()`, etc. |
| `cudnnPoolingForward()` | `aclnnMaxPool2d()`, `aclnnAvgPool2d()` |
| `cudnnBatchNormalizationForward()` | `aclnnBatchNorm()` |

## Advantages of `aclnn`
- **No Descriptors**: `aclnn` directly consumes `aclTensor` objects, which contain the shape, stride, and format data natively, reducing boilerplate code.
- **Host Dispatch**: The `aclnn` APIs are heavily optimized for minimal Host-side dispatch overhead.
