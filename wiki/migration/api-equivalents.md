---
id: migration-api-equivalents
title: "CUDA API → AscendC/AscendCL API Equivalents Reference"
type: wiki-migration
tags: [api, migration, reference, equivalents]
confidence: source-reported
sources: [doc-ascendc-api-reference, blog-ascendc-programming-guide]
from_concept: "CUDA Runtime/Driver API"
to_concept: "AscendC/AscendCL API"
difficulty: moderate
related: [migration-cuda-to-ascendc, lang-ascendc-guide]
---

## Overview

This reference maps CUDA Runtime and Driver APIs to their AscendC (kernel-level) and AscendCL (runtime-level) equivalents. Use this as a lookup table during CUDA → AscendC migration.

## Compute APIs

### Element-wise Operations

| CUDA Operation | AscendC API | Notes |
|---------------|-------------|-------|
| `z = a + b` (per-thread) | `Add(dst, src0, src1, count)` | Vector unit SIMD operation; operates on LocalTensor |
| `z = a * b` | `Mul(dst, src0, src1, count)` | Vector unit SIMD |
| `z = a - b` | `Sub(dst, src0, src1, count)` | Vector unit SIMD |
| `z = a / b` | `Div(dst, src0, src1, count)` | Vector unit SIMD |
| `z = sqrt(a)` | `Sqrt(dst, src, count)` | Vector unit SIMD |
| `z = exp(a)` | `Exp(dst, src, count)` | Vector unit SIMD |
| `z = log(a)` | `Ln(dst, src, count)` | Vector unit SIMD |
| `z = pow(a, b)` | `Pow(dst, a, b, count)` | Vector unit SIMD |
| `z = max(a, b)` | `Max(dst, a, b, count)` | Vector unit SIMD |
| `z = min(a, b)` | `Min(dst, a, b, count)` | Vector unit SIMD |
| `z = abs(a)` | `Abs(dst, src, count)` | Vector unit SIMD |

### Matrix Operations

| CUDA Operation | AscendC API | Notes |
|---------------|-------------|-------|
| `wmma::load_matrix_sync()` | `LocalTensor<T> src = queue.DeQue<T>()` | Load from UB queue to L0 |
| `wmma::mma_sync()` | `Matmul::Compute()` | Cube unit operation; requires NZ format |
| `wmma::store_matrix_sync()` | `queue.EnQue(dst)` | Store from L0 to UB queue |
| `cublasGemmEx()` | AscendCL blas GEMM (not AscendC) | Use high-level BLAS library |
| `cutlass::gemm()` | Catlass GEMM (not AscendC) | Modular GEMM framework for Ascend |

### Reduction Operations

| CUDA Operation | AscendC API | Notes |
|---------------|-------------|-------|
| Warp-level reduction (`warp_reduce_sum`) | `ReduceSum(dst, src, count)` | Vector unit reduction |
| Block-level reduction (`block_reduce_sum`) | `ReduceSum(dst, src, count)` + PipeBarrier | Single-AICore reduction |
| `atomicAdd(&ptr, val)` | No direct equivalent | Use Vector ReduceSum + manual atomic on host |
| `atomicExch()` | No direct equivalent | Not supported; redesign algorithm |

## Memory APIs

### Data Movement

| CUDA Operation | AscendC API | Notes |
|---------------|-------------|-------|
| `cudaMemcpy(dst, src, size, cudaMemcpyDeviceToDevice)` | `DataCopy(dst, src, count)` | GM ↔ UB transfer (MTE engine) |
| `cudaMemcpyAsync()` | `DataCopy()` + queue operations | Implicit async via queue model |
| `cudaMemcpy2D()` | `DataCopy()` with stride calculation | Manual stride handling |
| `cudaMemcpy3D()` | Multiple `DataCopy()` calls for each slice | Manual 3D decomposition |

### Memory Allocation

| CUDA Operation | AscendC API | Notes |
|---------------|-------------|-------|
| `cudaMalloc(&ptr, size)` | `acldrvMalloc` (AscendCL runtime) | Host-side GM allocation |
| `__shared__ float buf[N]` | `pipe.InitBuffer(que, 1, N*sizeof(T))` | UB allocation via TPipe |
| `float* reg_ptr = ...` (register) | `LocalTensor<T> local = queue.AllocTensor<T>()` | L0 allocation for compute |

### Memory Access Patterns

| CUDA Operation | AscendC API | Notes |
|---------------|-------------|-------|
| `__ldg(&ptr[idx])` (read-only cache) | `DataCopyPad()` with pad options | UB copy with padding for alignment |
| `ptr[idx]` (cached global read) | `GlobalTensor<T> gm[...]` | Direct GM access (cached via L1/L2) |
| `__restrict__` qualifier | No equivalent | Compiler optimization; rely on explicit queue management |

## Synchronization APIs

### Thread Synchronization

| CUDA Operation | AscendC API | Notes |
|---------------|-------------|-------|
| `__syncthreads()` | `PipeBarrier<PIPE_ALL>()` | All-queue barrier (CopyIn/Compute/CopyOut) |
| `__syncwarp()` | `PipeBarrier<PIPE_VEC>()` | Vector queue barrier only |
| `__threadfence()` | `PipeBarrier<PIPE_MTE>()` | MTE (memory transfer) queue barrier |
| `cudaDeviceSynchronize()` | `aclrtSynchronize` (AscendCL) | Device-level sync |

### Cooperative Groups

| CUDA Operation | AscendC API | Notes |
|---------------|-------------|-------|
| `cooperative_groups::this_thread_block()` | Single AICore context | No thread groups; AICore is unit |
| `cooperative_groups::wait()` | `SyncAll()` | Cross-core sync via AICCPU assistance |
| `cooperative_groups::sync()` | `PipeBarrier<PIPE_ALL>()` | Queue-based barrier |

## Stream and Event APIs

| CUDA Operation | AscendCL API | Notes |
|---------------|-------------|-------|
| `cudaStreamCreate(&stream)` | `aclrtCreateStream` | AscendCL stream management |
| `cudaStreamSynchronize(stream)` | `aclrtSynchronizeStream` | Stream synchronization |
| `cudaEventCreate(&event)` | `aclrtCreateEvent` | Event creation |
| `cudaEventRecord(event, stream)` | `aclrtRecordEvent` | Event recording |

## Library Equivalents

### Linear Algebra

| CUDA Library | Ascend Equivalent | Notes |
|-------------|------------------|-------|
| cuBLAS | AscendCL BLAS | High-level BLAS; not AscendC kernel-level |
| cuSolver | AscendCL Solver | Dense/sparse linear algebra |
| cuSPARSE | AscendCL SPARSE | Sparse matrix operations |

### Deep Learning

| CUDA Library | Ascend Equivalent | Notes |
|-------------|------------------|-------|
| cuDNN | AscendCL NN | Convolution, pooling, activation, normalization |
| cuTENSOR | AscendCL Tensor Operations | Tensor transformations and reductions |

### Communication

| CUDA Library | Ascend Equivalent | Notes |
|-------------|------------------|-------|
| NCCL | HCCL | Collective communication (AllReduce, Broadcast, etc.) |
| NVSHMEM | HCCS (Huawei Collective Communication) | PGAS-style communication |

### Performance Tools

| CUDA Library | Ascend Equivalent | Notes |
|-------------|------------------|-------|
| Nsight Compute | msprof | Kernel-level profiling |
| Nsight Systems | msprof | System-level tracing |
| nvprof | msprof --analytics | Command-line profiling |

### Custom GEMM Libraries

| CUDA Library | Ascend Equivalent | Notes |
|-------------|------------------|-------|
| CUTLASS | Catlass | Modular GEMM framework for Ascend |
| FlashAttention | FlashAttention-Ascend | Optimized attention kernels for Ascend |

## Kernel Launch and Management

| CUDA Operation | AscendCL API | Notes |
|---------------|-------------|-------|
| `kernel<<<grid, block>>>(args)` | `aclInvokeOp` | Launch compiled AscendC operator |
| `cudaLaunchKernel()` | `aclInvokeOp` | Explicit kernel launch |
| `cudaGetDeviceCount()` | `aclrtGetDeviceCount` | Query device count |
| `cudaSetDevice()` | `aclrtSetDevice` | Set current device |
| `cudaGetDeviceProperties()` | `aclrtGetDeviceProperties` | Query device capabilities |

## Memory Management (Runtime)

| CUDA Operation | AscendCL API | Notes |
|---------------|-------------|-------|
| `cudaMallocManaged(&ptr, size)` | `acldrvMalloc` + `aclrtMemcpy` | Manual memory management (no unified memory) |
| `cudaFree(ptr)` | `acldrvFree` | Free GM memory |
| `cudaMemGetInfo(&free, &total)` | `aclrtGetMemInfo` | Query memory usage |
| `cudaMallocHost(&ptr, size)` | `aclrtMallocHost` | Pinned memory allocation |
| `cudaHostAlloc(&ptr, size, flags)` | `aclrtMallocHost` | Pinned memory with flags |

## Error Handling

| CUDA Operation | AscendCL API | Notes |
|---------------|-------------|-------|
| `cudaGetLastError()` | `aclGetLastError` | Retrieve last error |
| `cudaPeekAtLastError()` | `aclPeekAtLastError` | Peek without clearing |
| `cudaGetErrorString(err)` | `aclGetErrorString` | Error description |

## Migration Notes

### 1. No Direct Atomic Operations
AscendC lacks direct equivalents for CUDA atomic operations (`atomicAdd`, `atomicExch`). **Workarounds**:
- Use Vector reduction APIs (ReduceSum, ReduceMax) for aggregations
- Perform reduction on single AICore, then write final result to GM
- Redesign algorithms to avoid race conditions

### 2. NZ Format Requirement
Matrix operations (Cube unit) require NZ (fractal) format:
```cpp
// CUDA: Row-major layout
float A[16][16];  // A[i][j] at &A[i] + j

// AscendC: NZ format required for Matmul
LocalTensor<half> A_nz = /* Convert to NZ */;
Matmul::Compute(C_nz, A_nz, B_nz);
```

### 3. Queue-Based Synchronization
Unlike CUDA's thread-based sync, AscendC uses queue barriers:
```cpp
// CUDA
__syncthreads();

// AscendC
PipeBarrier<PIPE_ALL>();  // Barrier across all queues
```

### 4. Higher-Level Operations Use AscendCL
For BLAS, DNN, and other high-level operations, use AscendCL libraries instead of writing AscendC kernels. Direct equivalents:
- `cublasSgemm()` → `aclblasGemmEx()` (AscendCL BLAS)
- `cudnnConvolutionForward()` → `aclnnConvForward()` (AscendCL NN)

## Reference Implementation

For complete migration examples, see:
- [migration-cuda-to-ascendc](/Users/haiyan/Documents/Infinity/Agent4Kernel/Ascend-KernelWiki-Q/wiki/migration/cuda-to-ascendc.md) for step-by-step kernel porting
- [lang-ascendc-guide](/Users/haiyan/Documents/Infinity/Agent4Kernel/Ascend-KernelWiki-Q/wiki/languages/ascendc-guide.md) for AscendC API usage
