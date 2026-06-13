---
id: migration-cutlass-to-catlass
title: "CUTLASS → Catlass Migration Guide"
type: wiki-migration
tags: [cutlass, catlass, migration, gemm, framework]
confidence: inferred
sources: [doc-catlass-framework, blog-ascendc-performance-tips]
from_concept: "CUTLASS GEMM"
to_concept: "Catlass GEMM"
difficulty: moderate
related: [kernel-matmul-ascendc, kernel-grouped-gemm-ascendc, migration-cuda-to-ascendc]
---

# CUTLASS to Catlass Migration Guide

Systematic mapping from NVIDIA CUTLASS concepts to Ascend Catlass framework for GEMM kernel development.

## Core Concept Mapping

| CUTLASS Concept | Catlass Equivalent | Notes |
|----------------|-------------------|-------|
| `cutlass::gemm::device::Gemm` | Catlass GEMM template | Main kernel entry point |
| `cutlass::gemm::GemmKernel::Params` | Catlass parameter struct | Kernel configuration structure |
| CollectiveMainloop (MMA + load) | Cube Matmul + MTE DataCopy pipeline | Compute + memory pipeline |
| CollectiveEpilogue | Vector epilogue | Post-processing ops |
| `cutlass::KernelHardwareInfo::sm_count` | AICore count | Parallel execution units |
| SMEM (shared memory tiles) | UB tile allocation | On-chip memory hierarchy |
| WGMMA instructions | Cube Matmul API | Matrix multiplication primitive |

## Key Architectural Differences

### 1. Mandatory NZ Format

**CUTLASS**: Accepts row-major (RC) or column-major (CM) layouts
**Catlass**: Requires FRACTAL_NZ format for all matrix operands

**Migration Impact**:
```cpp
// CUTLASS (row-major)
using LayoutA = cutlass::layout::RowMajor;
using LayoutB = cutlass::layout::RowMajor;

// Catlass (NZ format mandatory)
auto A_nz = ConvertToNZ(A_row_major);  // Must convert
auto B_nz = ConvertToNZ(B_row_major);
Matmul(A_nz, B_nz, C_nz, M, N, K);
```

### 2. Explicit Memory Hierarchy

**CUTLASS**: GM → SMEM → Registers (implicit in threadblock/iterator patterns)
**Catlass**: GM → L1 → UB → L0 (explicit `DataCopy` operations)

**Migration Impact**:
```cpp
// CUTLASS (implicit)
cutlass::gemm::GemmUniversalMode::kBatched;  // Framework handles memory

// Catlass (explicit)
DataCopy(gm_A, L1_A, tile_size);  // GM to L1
DataCopy(L1_A, UB_A, tile_size);   // L1 to UB
Matmul(UB_A, UB_B, UB_C);          // Compute in UB
```

### 3. Pipeline API Differences

**CUTLASS**: Pipeline classes (`Pipeline` vs `PipelineAsync`) for producer-consumer sync
**Catlass**: TPipe API with `PipeBarrier()`

**Migration Impact**:
```cpp
// CUTLASS
using Pipeline = cutlass::PipelineAsync<4>;
Pipeline pipeline(shared_storage);
pipeline.producer_acquire(index);
// ... load
pipeline.consumer_release(index);

// Catlass
PipeBarrier();  // Simple barrier between queue stages
```

### 4. Execution Unit Granularity

**CUTLASS**: Warp-level (32 threads) and threadblock-level (128/256 threads) concepts
**Catlass**: Entire AICore as single execution unit (no warp concept)

**Migration Impact**:
```cpp
// CUTLASS (warp-level)
using WarpMma = cutlass::gemm::warp::MmaTensorCore;

// Catlass (AICore-level)
Matmul(A_ub, B_ub, C_ub, M, N, K);  // Entire AICore operates on tile
```

## Epilogue Migration

### CUTLASS Epilogue Pattern
```cpp
// CUTLASS epilogue
using Epilogue = cutlass::epilogue::thread::LinearCombination<
    ElementOutput,                   // Output element type
    128 / cutlass::sizeof_bits<ElementOutput>::value,  // Elements per vector
    ElementAccumulator,              // Accumulator type
    ElementCompute>                  // Compute type
```

### Catlass Epilogue Equivalent
```ascendc
// Catlass epilogue (Vector operations)
Process() {
    // Cube matmul
    Matmul(A_ub, B_ub, C_ub, M, N, K);
    
    // Vector epilogue
    PipeBarrier();
    Add(C_ub, bias_ub, C_ub, M*N);
    Activation(C_ub, C_ub, M*N);
    DataCopy(gm_C, C_ub, M*N);
}
```

## Migration Workflow

1. **Identify CUTLASS kernel type** (GEMM, grouped GEMM, convolution)
2. **Map data layouts**: Convert row-major/col-major to NZ format
3. **Replace memory management**: SMEM → UB with explicit DataCopy
4. **Rewrite pipeline**: CUTLASS Pipeline → TPipe + PipeBarrier
5. **Port epilogue**: CUTLASS epilogue classes → Vector queue operations
6. **Handle threadblock → AICore mapping**: Remove thread/warp indexing
7. **Validate correctness**: Small test cases before optimization

## Code Example: Simple GEMM

### CUTLASS Implementation
```cpp
using Gemm = cutlass::gemm::device::Gemm<
    float,                          // ElementA
    cutlass::layout::RowMajor,      // LayoutA
    float,                          // ElementB
    cutlass::layout::RowMajor,      // LayoutB
    float,                          // ElementC
    cutlass::layout::RowMajor       // LayoutC
>;
Gemm gemm_op;
cutlass::Status status = gemm_op(args);
```

### Catlass Equivalent
```ascendc
extern "C" __global__ void gemm_kernel(
    GMEM float* A, GMEM float* B, GMEM float* C,
    int M, int N, int K) {
    
    // Allocate UB buffers
    TBuf A_ub, B_ub, C_ub;
    
    // Load inputs in NZ format
    DataCopy(A, A_ub, M*K, ND_TO_NZ);
    DataCopy(B, B_ub, K*N, ND_TO_NZ);
    
    // Compute
    Matmul(A_ub, B_ub, C_ub, M, N, K);
    
    // Store output
    DataCopy(C_ub, C, M*N, NZ_TO_ND);
}
```

## Performance Considerations

**NZ format overhead**: ~6% memory expansion vs row-major

**Pipeline overlap**: Catlass requires more explicit queue management than CUTLASS's automatic pipeline

**Tile sizing**: Catlass UB sizes differ from CUTLASS SMEM sizes, requires re-tuning

## Debugging Tips

1. **Verify NZ conversion**: Check intermediate outputs after format conversion
2. **Validate dimensions**: Ensure M, N, K are multiples of 16
3. **Profile queue utilization**: Use msprof to check Vector/Cube overlap
4. **Start with small tiles**: Verify correctness before aggressive optimization

## Related Resources

- [MatMul on Ascend](kernel-matmul-ascendc) — native Ascend GEMM patterns
- [NZ Format Traps](pattern-nz-format-traps) — common migration pitfalls
- [Pipeline Scheduling](technique-pipeline-scheduling) — Ascend-specific pipeline optimization
- [CUDA to AscendC Migration](migration-cuda-to-ascendc) — broader CUDA migration guide
