---
id: technique-nz-tiling
title: "FRACTAL_NZ Tiling Strategy for Cube Unit"
type: wiki-technique
architectures: [ascend910, ascend910b]
tags: [nz-format, tiling, data-format, optimization]
confidence: source-reported
techniques: [nz-tiling]
hardware_features: [nz-format, cube-unit]
related: [hw-cube-unit, technique-format-conversion]
sources: [blog-nz-format-explained, doc-catlass-framework]
reproducibility: snippet
---

# FRACTAL_NZ Tiling for Cube Unit Operations

The Ascend Cube Unit requires data in FRACTAL_NZ format—a 5D blocked layout optimized for matrix operations. NZ tiling is the strategy for partitioning and arranging matrix data to satisfy this hardware constraint while maximizing compute efficiency.

## FRACTAL_NZ Layout Structure

FRACTAL_NZ organizes tensors in a 5D structure: `(C1, H, C0, Ni, No)` where:

- **C1**: Coarse channel dimension (divided by C0)
- **H**: Spatial dimension (rows/cols in matrix context)
- **C0**: Fixed block size = 16 (channels/block)
- **Ni**: Inner block size = 16 (rows/block)
- **No**: Outer block size = 16 (cols/block)

For GEMM C = A × B with A (M×K) and B (K×N):
- A is reshaped to `(M, K)` → NZ: `(M1, 1, 16, 16, K1)` where K1 = K/16
- B is reshaped to `(K, N)` → NZ: `(K1, 1, 16, N1, 16)` where N1 = N/16

## Tiling Strategy for GEMM

```cpp
template<typename T>
void NZTiledGEMM(int M, int N, int K) {
    // Pad dimensions to NZ-friendly sizes
    int M_padded = ((M + 15) / 16) * 16;
    int N_padded = ((N + 15) / 16) * 16;
    int K_padded = ((K + 15) / 16) * 16;
    
    // Tile sizes must be multiples of 16
    const int tile_M = 128;  // 8 × 16
    const int tile_N = 128;  // 8 × 16
    const int tile_K = 64;   // 4 × 16
    
    for (int m = 0; m < M_padded; m += tile_M) {
        for (int n = 0; n < N_padded; n += tile_N) {
            for (int k = 0; k < K_padded; k += tile_K) {
                // Load A[m:m+tile_M, k:k+tile_K] in NZ format
                LoadNZTile(bufferA, GM_A, m, k, tile_M, tile_K);
                
                // Load B[k:k+tile_K, n:n+tile_N] in NZ format
                LoadNZTile(bufferB, GM_B, k, n, tile_K, tile_N);
                
                // Compute on NZ tiles (requires NZ input)
                pipe.Matmul(bufferA, bufferB, bufferC, tile_M, tile_N, tile_K);
                
                // Store result (C is automatically in NZ format)
                StoreNZTile(GM_C, bufferC, m, n, tile_M, tile_N);
            }
        }
    }
}
```

## NZ Format Conversion

ND (N-dimensional) to NZ conversion overhead can be significant:

```cpp
// ND → NZ conversion
void ConvertToNZ(const T* nd_data, T* nz_data, int rows, int cols) {
    // Iterate over NZ blocks
    for (int i = 0; i < rows; i += 16) {
        for (int j = 0; j < cols; j += 16) {
            // Transpose within 16×16 block for NZ layout
            for (int bi = 0; bi < 16; bi++) {
                for (int bj = 0; bj < 16; bj++) {
                    nz_data[GetNZIndex(i+bi, j+bj)] = nd_data[(i+bi)*cols + (j+bj)];
                }
            }
        }
    }
}
```

## Optimization: Keep Data in NZ

Key strategy: maintain NZ format throughout pipeline stages to avoid repeated conversion:

1. **Input Preparation**: Convert input tensors from ND to NZ once (kernel prologue)
2. **Compute Pipeline**: All intermediate results stay in NZ format
3. **Output**: Convert final result from NZ to ND (kernel epilogue)

For multi-GEMM pipelines (e.g., attention: Q@K, then attn@V), keeping intermediate activations in NZ format eliminates redundant conversions.

## Performance Considerations

- **Padding Overhead**: NZ requires dimensions padded to 16× multiples
- **Conversion Cost**: ND↔NZ conversion adds ~10-15% overhead for single GEMM
- **Memory Access Pattern**: NZ layout optimizes Cube Unit's 16×16 block processing
- **Cache Efficiency**: Regular 16×16 blocks improve L2 cache utilization

On Ascend 910B, NZ-formatted GEMM achieves ~80% of theoretical peak TFLOPS, compared to ~50% for naive ND-formatted implementations.
