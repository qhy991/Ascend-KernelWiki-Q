---
id: migration-rocm-to-ascendc
title: "ROCm (HIP) to AscendC Migration"
type: wiki-migration
tags:
  - framework
  - rocm
confidence: inferred
sources: []
---

# ROCm (HIP) to AscendC Migration

Migrating kernels from AMD ROCm (HIP) to AscendC requires a fundamental shift in programming model. While HIP is heavily modeled after CUDA (SIMT architecture), AscendC is built on the Da Vinci architecture (SIMD / Matrix-first architecture).

## Conceptual Mapping

| Concept | AMD ROCm (HIP) | Huawei Ascend (AscendC) |
| :--- | :--- | :--- |
| **Execution Model** | SIMT (Single Instruction, Multiple Threads) | SIMD / Pipeline (Vector + Cube Units) |
| **Workgroup** | `threadIdx`, `blockIdx` | No threads. Only AI Cores (`blockDim`). |
| **Matrix Core** | MFMA (Matrix Fused Multiply-Add) | Cube Unit (Da Vinci Matrix Engine) |
| **Shared Memory** | LDS (Local Data Share) | Unified Buffer (UB) |
| **Registers** | Massive VGPR/SGPR files | L0A / L0B / L0C buffers + limited registers |
| **Warp/Wavefront**| Wavefront (Wave64 or Wave32) | N/A. Entire Vector Unit acts as one massive 256-byte SIMD vector. |

## Key Differences

### 1. Goodbye Threads, Hello Tensors
In HIP, you write code from the perspective of a single thread (e.g., `int idx = threadIdx.x`). In AscendC, you write code from the perspective of a pipeline manager moving Tensor chunks. You never manipulate individual elements; you issue instructions on `LocalTensor` blocks.

### 2. LDS vs Unified Buffer
ROCm LDS is highly banked. If multiple threads access the same bank, a bank conflict stalls the wavefront.
Ascend UB is a massive SRAM scratchpad. Instead of worrying about bank conflicts, you must worry about **DMA Latency**. Data must be explicitly moved from Global Memory to UB using `DataCopy` via the MTE engine before the Vector unit can touch it.

### 3. MFMA vs Cube Unit
ROCm MFMA instructions require complex register layouts and shuffling (Wave Matrix Multiply). 
Ascend's Cube unit is drastically simpler to program but more rigid. You use `DataCopy` to move data into L0A and L0B, then call `Matmul`. The hardware handles the systolic array scheduling completely invisibly.
