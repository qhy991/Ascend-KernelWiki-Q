---
id: kernel-matmul-ascendc
title: "AscendC Matmul — GEMM via Cube Unit and Catlass"
type: wiki-kernel
architectures: [ascend910, ascend910b]
tags: [matmul, gemm, cube-unit, ascendc]
confidence: source-reported
kernel_types: [matmul, gemm]
languages: [ascendc]
related: [wiki-hardware-cube-unit, technique-pipeline-scheduling, technique-nz-tiling]
sources: [doc-ascendc-api-reference, doc-catlass-framework]
performance_claims:
  - gpu: Ascend 910B
    dtype: fp16
    shape: "M=4096, N=4096, K=4096"
    metric: TFLOPS
    value: 256
    utilization: "~80%"
    source_id: doc-catlass-framework
  - gpu: Ascend 910A
    dtype: fp16
    shape: "M=4096, N=4096, K=4096"
    metric: TFLOPS
    value: 200
    utilization: "~78%"
    source_id: doc-catlass-framework
reproducibility: snippet
techniques: [pipeline-scheduling, nz-tiling, double-buffering]
operator_recipe:
  operator: matmul
  dtype: [fp16, bf16]
  layout: [ND, FRACTAL_NZ]
  shape_class: [large-square, batched, compute-bound]
  memory_path:
    global_memory: [A, B, C]
    onchip_buffers: [UB, L1, L0A, L0B, L0C]
    data_formats: [ND-input, FRACTAL_NZ-internal]
  parallelism:
    granularity: output tiles over M and N
    block_dim: AI Cube core count
    sync_scope: per-AICore independent output tile
  instruction_family: [Mmad, Matmul]
  library_backend: [AscendC Matmul, CATLASS]
  tiling:
    tile_axes: [M, N, K]
    tile_granularity: L1 block tiles and L0 Cube fragments
    constraints: [N-and-K-multiple-of-16, UB-L1-L0-capacity]
  pipeline:
    stages: [CopyIn, Mmad, CopyOut]
    queues: [MTE, Cube, Vector]
    overlap: double-buffered A/B tiles hide DataCopy behind Cube compute
  aicore_mapping:
    block_dim: aicCoreNum
    scheduling: block swizzle partitions MxN output tiles across AI Cube cores
  data_movement:
    apis: [DataCopy, LoadData]
    path: "GM -> UB/L1 -> L0A/L0B -> L0C -> GM"
  compute_path:
    units: [Cube Unit]
    primitives: [Matmul, Mmad]
---

# AscendC GEMM Implementation

AscendC GEMM kernels leverage the Cube Unit for matrix multiplication through the Catlass (Computing and Tensor Layout) framework. This implementation combines NZ format requirements, pipeline scheduling, and double buffering to achieve high throughput on Ascend NPUs.

## Catlass Framework Structure

Catlass organizes GEMM computation into three phases:

### 1. Prologue (Tile Loading)
```cpp
void GEMMPrologue(float16_t* GM_A, float16_t* GM_B, float16_t GM_C) {
    // Convert input matrices from ND to NZ format
    ConvertNDtoNZ(GM_A, NZ_A, M, K);
    ConvertNDtoNZ(GM_B, NZ_B, K, N);
    
    // Initialize pipeline buffers
    pipe.InitBuffer(bufferA, UB_SIZE_A, bufferB, UB_SIZE_B, bufferC, UB_SIZE_C);
}
```

### 2. Main Loop (Tiled Computation)
```cpp
void GEMMMainLoop() {
    for (int m_tile = 0; m_tile < M; m_tile += TILE_M) {
        for (int n_tile = 0; n_tile < N; n_tile += TILE_N) {
            for (int k_tile = 0; k_tile < K; k_tile += TILE_K) {
                // Double buffer index
                int buf_idx = (k_tile / TILE_K) % 2;
                
                // Load tiles with pipeline scheduling
                pipe.DataCopy(bufferA[buf_idx], NZ_A + GetNZOffset(m_tile, k_tile));
                pipe.DataCopy(bufferB[buf_idx], NZ_B + GetNZOffset(k_tile, n_tile));
                
                // Compute on previous tile (while current loads)
                if (k_tile > 0) {
                    int prev_idx = 1 - buf_idx;
                    pipe.Matmul(bufferA[prev_idx], bufferB[prev_idx], bufferC, 
                               TILE_M, TILE_N, TILE_K);
                }
                
                // Write completed result
                if (k_tile > TILE_K) {
                    pipe.DataCopy(NZ_C + GetNZOffset(m_tile, n_tile), bufferC);
                }
            }
        }
    }
}
```

### 3. Epilogue (Result Storage)
```cpp
void GEMMEpilogue() {
    // Convert result from NZ to ND format
    ConvertNZtoND(NZ_C, GM_C, M, N);
}
```

## Simplified AscendC Matmul API Usage

```cpp
extern "C" __global__ __aicore__ void gemm_kernel(
    __gm__ uint8_t* GM_A, __gm__ uint8_t* GM_B, __gm__ uint8_t* GM_C,
    int M, int N, int K) {
    
    TPipe pipe;
    LocalTensor<half> A, B, C;
    
    // Allocate Unified Buffer
    A = AllocUB<half>(TILE_M * TILE_K);
    B = AllocUB<half>(TILE_K * TILE_N);
    C = AllocUB<half>(TILE_M * TILE_N);
    
    // NZ format loading
    DataCopy(A, GM_A, {M, K});
    DataCopy(B, GM_B, {K, N});
    
    // Matrix multiplication (Cube Unit)
    Matmul(C, A, B, {M, N, K}, {TILE_M, TILE_N, TILE_K});
    
    // Store result
    DataCopy(GM_C, C, {M, N});
}
```

## Performance on Ascend Hardware

| GPU       | Shape (M×N×K) | Data Type | TFLOPS | Utilization | Notes                        |
|-----------|---------------|-----------|--------|--------------|------------------------------|
| 910B      | 4096×4096×4096 | fp16      | 256    | ~80%         | Double buffering enabled      |
| 910A      | 4096×4096×4096 | fp16      | 200    | ~78%         | Catlass framework            |
| 910B      | 2048×2048×2048 | fp16      | 248    | ~77%         | Smaller tiles reduce overhead |
| 910B      | 1024×1024×1024 | fp32      | 128    | ~65%         | FP32 limited by memory       |

## Tuning Parameters

Key parameters for optimization:

- **Tile Sizes**: `TILE_M`, `TILE_N`, `TILE_K` typically multiples of 16 for NZ alignment
- **UB Allocation**: Balance tile size against 1MB UB capacity
- **Pipeline Stages**: 3-stage CopyIn→Compute→CopyOut for large tiles
- **Double Buffering**: Enable when UB capacity permits

## Implementation Notes

- **NZ Format Conversion**: Adds 10-15% overhead; keep data in NZ when possible
- **Cube Unit Utilization**: Requires careful tile sizing to avoid pipeline stalls
- **Memory Alignment**: GM addresses must be 32-byte aligned for optimal MTE performance
- **Numerical Accuracy**: FP16 GEMM uses accumulation in FP32 for stability
