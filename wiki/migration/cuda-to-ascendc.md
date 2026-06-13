---
id: migration-cuda-to-ascendc
title: "CUDA → AscendC Migration Guide"
type: wiki-migration
tags: [migration, cuda, ascendc, porting]
confidence: inferred
sources: [blog-ascendc-programming-guide, doc-ascendc-api-reference]
from_concept: "CUDA C++ Kernel"
to_concept: "AscendC Kernel"
difficulty: hard
related: [migration-memory-model-mapping, migration-api-equivalents]
---

## Overview

Migrating from CUDA to AscendC requires significant architectural changes due to fundamental differences in execution model, memory hierarchy, and programming paradigm. This guide provides a structured approach for porting CUDA kernels to AscendC.

## Concept Mapping Table

| CUDA Concept | AscendC Equivalent | Migration Notes |
|-------------|-------------------|-----------------|
| `__global__` kernel | `__aicore__` class Process() | Wrap kernel in class with Init/Process methods; no `__global__` qualifier |
| Grid/Block/Thread hierarchy | Multi-core SPMD + tile-based processing | Each AICore runs same code; use GetBlockIdx() for core ID, process tiles instead of per-thread elements |
| `__shared__` memory | Unified Buffer (UB) | Explicit allocation via TPipe/TBuf APIs; not declarative like `__shared__` |
| Global memory | Global Memory (GM) | Similar HBM, accessed via GlobalTensor<T> with SetGlobalBuffer() |
| Thread-private registers | L0 Buffer (Cube/Vector operands) | Implicit allocation for compute operands |
| `__syncthreads()` | PipeBarrier / SyncAll | Queue-based synchronization; use PipeBarrier for queue stages, SyncAll for cross-core |
| WMMA/MMA (Tensor Core) | Cube Matmul API | Different API surface; requires NZ (N-dimensional) format |
| CUDA cores (SIMT) | Vector unit (SIMD) | Different programming model — explicit SIMD ops vs implicit per-thread |
| cudaMemcpy | DataCopy() | MTE engine; asynchronous via queues; explicit enqueue/dequeue |
| warp shuffle (32-thread) | No direct equivalent | Use Vector reduction APIs (ReduceSum, ReduceMax) instead |
| cooperative_groups | SyncAll() | Cross-core sync via AICPU-assisted barrier |
| cudaStream_t | Multiple TPipe queues | Vector, Cube, Scalar, MTE queues for parallelism |

## Migration Steps

### Step 1: Convert Kernel Function → AscendC Class

**Before (CUDA)**:
```cpp
__global__ void vector_add(float* x, float* y, float* z, int N) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < N) z[idx] = x[idx] + y[idx];
}
```

**After (AscendC)**:
```cpp
class VectorAdd {
public:
    __aicore__ void Init(GM_ADDR x, GM_ADDR y, GM_ADDR z, uint32_t N) {
        // Set global buffers
        xGm.SetGlobalBuffer((__gm__ float*)x, N);
        yGm.SetGlobalBuffer((__gm__ float*)y, N);
        zGm.SetGlobalBuffer((__gm__ float*)z, N);
        // Allocate UB queues
        pipe.InitBuffer(inQueueX, 1, N * sizeof(float));
        pipe.InitBuffer(inQueueY, 1, N * sizeof(float));
        pipe.InitBuffer(outQueueZ, 1, N * sizeof(float));
    }
    
    __aicore__ void Process() {
        // CopyIn: GM → UB
        LocalTensor<float> xLocal = inQueueX.AllocTensor<float>();
        LocalTensor<float> yLocal = inQueueY.AllocTensor<float>();
        DataCopy(xLocal, xGm, N);
        DataCopy(yLocal, yGm, N);
        inQueueX.EnQue(xLocal);
        inQueueY.EnQue(yLocal);

        // Compute: Vector Add
        xLocal = inQueueX.DeQue<float>();
        yLocal = inQueueY.DeQue<float>();
        LocalTensor<float> zLocal = outQueueZ.AllocTensor<float>();
        Add(zLocal, xLocal, yLocal, N);
        outQueueZ.EnQue<float>(zLocal);

        // CopyOut: UB → GM
        zLocal = outQueueZ.DeQue<float>();
        DataCopy(zGm, zLocal, N);
    }
private:
    TPipe pipe;
    TQue<QuePosition::VECIN, 1> inQueueX, inQueueY;
    TQue<QuePosition::VECOUT, 1> outQueueZ;
    GlobalTensor<float> xGm, yGm, zGm;
    uint32_t N;
};
```

### Step 2: Replace Shared Memory → UB Allocation

**CUDA**: `__shared__ float tile[128];`

**AscendC**: 
```cpp
TPipe pipe;
TQue<QuePosition::VECIN, 1> inQueue;
pipe.InitBuffer(inQueue, 1, 128 * sizeof(float));
LocalTensor<float> tile = inQueue.AllocTensor<float>();
```

### Step 3: Replace Thread Indexing → Tile-Based Processing

**CUDA**: `int idx = blockIdx.x * blockDim.x + threadIdx.x;`

**AscendC**: `uint32_t block_idx = GetBlockIdx(); uint32_t tile_size = 32; // Process tiles of 32 elements`

### Step 4: Replace Tensor Core → Cube Matmul API

**CUDA (WMMA)**:
```cpp
nvcuda::wmma::fragment<nvcuda::wmma::matrix_a, 16, 16, 16, half, nvcuda::wmma::row_major> a_frag;
nvcuda::wmma::load_matrix_sync(a_frag, a_ptr, 16);
nvcuda::wmma::mma_sync(d_frag, a_frag, b_frag, c_frag);
```

**AscendC (Cube)**:
```cpp
// Data must be in NZ format (fractal transformation)
LocalTensor<half> a_local = /* NZ-formatted A */;
LocalTensor<half> b_local = /* NZ-formatted B */;
LocalTensor<float> c_local = /* NZ-formatted C */;
Matmul<float, half, half> matmul;
matmul.Init(c_local, a_local, b_local);
matmul.Compute();
```

**Critical**: Convert data to NZ format before Matmul, or keep in NZ throughout pipeline.

### Step 5: Replace Synchronization → PipeBarrier

**CUDA**: `__syncthreads();`

**AscendC**: `PipeBarrier<PIPE_ALL>();` // All queues barrier

### Step 6: Handle NZ Format

AscendC uses NZ (N-dimensional fractal) format for Cube operations, unlike CUDA's row-major layout:

1. **Convert ND → NZ**: Use NZ format conversion APIs before Matmul
2. **Keep NZ throughout**: Avoid frequent conversions; keep intermediate results in NZ
3. **Use NZ-aware APIs**: DataCopyNZ, SetGlobalBufferNZ for NZ-aware transfers

## Common Patterns and Their AscendC Equivalents

| CUDA Pattern | AscendC Pattern |
|-------------|----------------|
| Cooperative tile loading with __syncthreads() | Queue-based CopyIn/Compute/CopyOut pipeline with PipeBarrier |
| Warp-level reduction (warp shuffle) | Vector ReduceSum/ReduceMax with explicit sync |
| Tensor Core GEMM with tiling | Cube Matmul with NZ-formatted tiles |
| Dynamic shared memory | Dynamic buffer allocation in Init() |
| Multi-stream concurrency | Multiple TPipe queues (Vec/Cube/MTE) for parallelism |

## Testing and Verification

1. **Unit test per tile**: Verify correctness for single tile before scaling
2. **Cross-core sync validation**: Test SyncAll() with multiple AICores
3. **Performance profiling**: Use msprof to identify queue bottlenecks
4. **NZ format validation**: Compare NZ-converted output against ND reference

## Tools and Resources

- **AscendC Compiler**: `aicll` for compilation
- **Profiling**: `msprof` for performance analysis
- **Reference**: [lang-ascendc-guide](/Users/haiyan/Documents/Infinity/Agent4Kernel/Ascend-KernelWiki-Q/wiki/languages/ascendc-guide.md) for API details
- **Memory mapping**: [migration-memory-model-mapping](/Users/haiyan/Documents/Infinity/Agent4Kernel/Ascend-KernelWiki-Q/wiki/migration/memory-model-mapping.md) for memory hierarchy translation
