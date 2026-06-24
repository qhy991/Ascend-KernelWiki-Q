---
id: migration-memory-model-mapping
title: "CUDA Memory Model → Ascend Memory Model Mapping"
type: wiki-migration
tags: [memory, migration, shared-memory, unified-buffer]
confidence: inferred
sources: [doc-ascend-memory-hierarchy, blog-ascendc-programming-guide]
from_concept: "CUDA Memory Hierarchy"
to_concept: "Ascend Memory Hierarchy"
difficulty: moderate
related: [migration-cuda-to-ascendc, hw-memory-hierarchy]
---

## Overview

CUDA and Ascend have different memory hierarchies but share similar architectural principles. Understanding the mapping between memory spaces is critical for successful migration from CUDA to AscendC.

## Memory Space Mapping

| CUDA Memory | Ascend Memory | Characteristics | Key Difference |
|-------------|---------------|-----------------|----------------|
| Global Memory | Global Memory (GM) | HBM, large capacity, high latency | Similar semantic; accessed via GlobalTensor<T> in AscendC |
| Shared Memory | Unified Buffer (UB) | On-chip, software-managed, fast | **Critical**: UB requires explicit TPipe/TBuf allocation; not declarative like `__shared__` |
| Registers | L0 Buffer | Operand storage for compute units | Implicit in AscendC; allocated for Cube/Vector ops |
| L1 Cache | L1 Buffer | Optional staging area | Less explicit; UB usage preferred |
| Constant Memory | No direct equivalent | Read-only cache | Use UB with constant values instead |
| Texture Memory | No direct equivalent | Read-only spatial cache | Not applicable; use UB caching |
| Local Memory | GM overflow | Spill to GM when UB insufficient | Use larger UB allocation to avoid |

## Detailed Comparison

### Global Memory (GM)

**CUDA**: `__device__ float* global_ptr;` accessed directly in kernels

**AscendC**: Explicit GlobalTensor setup:
```cpp
GlobalTensor<half> xGm;
xGm.SetGlobalBuffer((__gm__ half*)x_addr, length);
```

**Similarities**: Both reside in HBM, high latency, large capacity

**Differences**: AscendC requires explicit buffer binding before use

### Shared Memory → Unified Buffer (Critical Mapping)

**CUDA** (Declarative, per-block):
```cpp
__global__ void kernel() {
    __shared__ float tile[128];  // Allocated at kernel launch
    int idx = threadIdx.x;
    tile[idx] = global_ptr[idx];
    __syncthreads();
    // Use tile...
}
```

**AscendC** (Explicit queue-based allocation):
```cpp
class Kernel {
public:
    __aicore__ void Init() {
        // Explicit UB allocation via TPipe
        TPipe pipe;
        TQue<QuePosition::VECIN, 1> inQueue;
        pipe.InitBuffer(inQueue, 1, 128 * sizeof(float));
    }
    
    __aicore__ void Process() {
        // Allocate from queue
        LocalTensor<float> tile = inQueue.AllocTensor<float>();
        DataCopy(tile, global_tensor, 128);
        inQueue.EnQue(tile);
        
        // Use tile...
        LocalTensor<float> tile_use = inQueue.DeQue<float>();
    }
};
```

**Key Differences**:
1. **Allocation model**: CUDA uses static declaration; AscendC uses dynamic queue allocation
2. **Scope**: CUDA shared memory is per-block; AscendC UB is per-AICore
3. **Synchronization**: CUDA uses `__syncthreads()`; AscendC uses queue operations (EnQue/DeQue) + PipeBarrier
4. **Lifetime**: CUDA shared memory persists across sync; AscendC UB is managed via queues with explicit flow

### Registers → L0 Buffer

**CUDA**: Implicit register allocation by compiler; e.g., `float reg = data[idx];`

**AscendC**: Implicit L0 allocation for compute operands:
```cpp
LocalTensor<half> x = inQueue.DeQue<half>();  // L0 allocation for Vector unit
Add(z, x, y, length);  // L0 operands used implicitly
```

**Note**: Developers don't directly manage L0; it's allocated automatically for compute operations.

### Constant Memory Replacement

**CUDA**: `__constant__ float params[16];` accessed with cached reads

**AscendC**: Use UB with scalar values:
```cpp
// Load constants into UB once
LocalTensor<float> constants = ub_queue.AllocTensor<float>();
DataCopy(constants, gm_constants, 16);
ub_queue.EnQue(constants);

// Reuse constants across iterations
LocalTensor<float> c = ub_queue.DeQue<float>();
Mul(out, in, c, length);  // Broadcast multiply
ub_queue.EnQue(c);  // Re-enqueue for reuse
```

## Code Comparison: Shared Memory Pattern

### CUDA Cooperative Tile Loading

```cpp
__global__ void matmul_tiled(float* A, float* B, float* C, int N) {
    __shared__ float tile_A[32][32];
    __shared__ float tile_B[32][32];
    
    int row = blockIdx.y * 32 + threadIdx.y;
    int col = blockIdx.x * 32 + threadIdx.x;
    
    float sum = 0.0f;
    for (int t = 0; t < N/32; ++t) {
        // Cooperative loading
        tile_A[threadIdx.y][threadIdx.x] = A[row * N + t * 32 + threadIdx.x];
        tile_B[threadIdx.y][threadIdx.x] = B[(t * 32 + threadIdx.y) * N + col];
        __syncthreads();
        
        // Compute
        for (int k = 0; k < 32; ++k) {
            sum += tile_A[threadIdx.y][k] * tile_B[k][threadIdx.x];
        }
        __syncthreads();
    }
    C[row * N + col] = sum;
}
```

### AscendC Queue-Based Tile Loading

```cpp
class MatmulTiled {
public:
    __aicore__ void Init(GM_ADDR A, GM_ADDR B, GM_ADDR C, int N) {
        aGm.SetGlobalBuffer((__gm__ float*)A, N * N);
        bGm.SetGlobalBuffer((__gm__ float*)B, N * N);
        cGm.SetGlobalBuffer((__gm__ float*)C, N * N);
        
        // Allocate UB queues for tiles
        pipe.InitBuffer(queueA, 1, 32 * 32 * sizeof(float));
        pipe.InitBuffer(queueB, 1, 32 * 32 * sizeof(float));
    }
    
    __aicore__ void Process() {
        LocalTensor<float> tileA = queueA.AllocTensor<float>();
        LocalTensor<float> tileB = queueB.AllocTensor<float>();
        
        for (int t = 0; t < N/32; ++t) {
            // CopyIn: GM → UB (single AICore loads entire tile)
            int a_offset = GetBlockIdx() * 32 * N + t * 32;
            int b_offset = t * 32 * N + blockIdx.x * 32;
            DataCopy(tileA, aGm[a_offset], 32 * 32);
            DataCopy(tileB, bGm[b_offset], 32 * 32);
            queueA.EnQue(tileA);
            queueB.EnQue(tileB);
            
            // Compute: Matmul on tiles
            tileA = queueA.DeQue<float>();
            tileB = queueB.DeQue<float>();
            LocalTensor<float> tileC = queueC.AllocTensor<float>();
            
            // Use Vector API for tiled computation
            for (int i = 0; i < 32; ++i) {
                for (int j = 0; j < 32; ++j) {
                    float sum = 0.0f;
                    for (int k = 0; k < 32; ++k) {
                        sum += tileA[i * 32 + k] * tileB[k * 32 + j];
                    }
                    tileC[i * 32 + j] = sum;
                }
            }
            queueC.EnQue(tileC);
        }
        
        // CopyOut: UB → GM
        LocalTensor<float> result = queueC.DeQue<float>();
        DataCopy(cGm, result, 32 * 32);
    }
private:
    TPipe pipe;
    TQue<QuePosition::VECIN, 1> queueA, queueB;
    TQue<QuePosition::VECOUT, 1> queueC;
    GlobalTensor<float> aGm, bGm, cGm;
    int N;
};
```

**Key Observations**:
1. **Cooperative vs Single-Core**: CUDA relies on 32 threads cooperatively loading tiles; AscendC single AICore loads entire tile
2. **Sync vs Queue**: CUDA uses `__syncthreads()`; AscendC uses EnQue/DeQue flow
3. **Tile ownership**: CUDA threads own elements within tile; AscendC AICore owns entire tile

## Migration Recommendations

1. **Design for tile-level parallelism**: Think in terms of AICores processing tiles, not threads processing elements
2. **Maximize UB reuse**: Keep data in UB across multiple compute stages (EnQue/DeQue doesn't deallocate)
3. **Use queues for pipeline parallelism**: Allocate multiple queues to overlap CopyIn/Compute/CopyOut
4. **Avoid UB fragmentation**: Pre-allocate large buffers and reuse via queue management
5. **Profile UB usage**: Use msprof to verify UB capacity isn't exceeded (typically 256KB-1MB per AICore)

## Performance Implications

| Aspect | CUDA | AscendC | Impact |
|--------|------|---------|--------|
| Shared memory allocation | Static (compile-time) | Dynamic (queue-based) | AscendC requires careful buffer sizing |
| Memory coalescing | Implicit in thread access patterns | Explicit DataCopy with stride | AscendC needs explicit stride handling |
| Bank conflicts | Hardware-managed | Less critical (SIMD) | Different optimization focus |
| Capacity limits | Per-block (e.g., 48KB) | Per-AICore (e.g., 256KB-1MB) | AscendC typically larger UB |

## Related Resources

- **Full migration guide**: [migration-cuda-to-ascendc](/Users/haiyan/Documents/Infinity/Agent4Kernel/Ascend-KernelWiki-Q/wiki/migration/cuda-to-ascendc.md)
- **AscendC API reference**: [lang-ascendc-guide](/Users/haiyan/Documents/Infinity/Agent4Kernel/Ascend-KernelWiki-Q/wiki/languages/ascendc-guide.md)
- **Hardware details**: [wiki-hardware-memory-hierarchy](/Users/haiyan/Documents/Infinity/Agent4Kernel/Ascend-KernelWiki-Q/wiki/hardware/memory-hierarchy.md)
