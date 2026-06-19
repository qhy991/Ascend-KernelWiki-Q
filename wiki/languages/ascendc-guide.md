---
id: lang-ascendc-guide
title: "AscendC Programming Guide — C/C++ Kernel Development for Ascend NPU"
type: wiki-language
tags: [ascendc, programming, kernel, tutorial]
confidence: source-reported
sources: [doc-ascendc-api-reference, blog-ascendc-programming-guide]
architectures: [ascend910, ascend910b, ascend310p]
languages: [ascendc]
related: [lang-tbe-dsl-guide, migration-cuda-to-ascendc, lang-ascendc-direct-launch-project, pattern-ascendc-compile-troubleshooting]
---

## Overview

AscendC is Huawei's C/C++-based programming language for custom operator development on Ascend NPUs. Introduced in CANN 7.0, it replaces the older TBE (TVM-based) approach with a more explicit, low-level programming model that gives developers fine-grained control over the Ascend AI Core (AICore) architecture.

## Execution Model

- **Kernel**: Each AICore runs one kernel instance using SPMD (Single Program Multiple Data) model — all cores execute the same code on different data tiles
- **Pipeline**: Three-stage execution pipeline — CopyIn (GM→UB) → Compute (UB operations) → CopyOut (UB→GM)
- **Memory Hierarchy**: Explicit management of Global Memory (GM) → Unified Buffer (UB) → L0 Buffer (Cube/Vector units)
- **Instruction Queues**: 4 independent queues for parallel execution — Scalar, Vector, Cube, and MTE (Memory Transfer Engine)

## Hello World — Vector Add

```cpp
#include "kernel_operator.h"

class AddKernel {
public:
    __aicore__ void Init(GM_ADDR x, GM_ADDR y, GM_ADDR z, uint32_t totalLength) {
        this->totalLength = totalLength;
        xGm.SetGlobalBuffer((__gm__ half*)x, totalLength);
        yGm.SetGlobalBuffer((__gm__ half*)y, totalLength);
        zGm.SetGlobalBuffer((__gm__ half*)z, totalLength);
        pipe.InitBuffer(inQueueX, 1, totalLength * sizeof(half));
        pipe.InitBuffer(inQueueY, 1, totalLength * sizeof(half));
        pipe.InitBuffer(outQueueZ, 1, totalLength * sizeof(half));
    }
    
    __aicore__ void Process() {
        // CopyIn: GM → UB
        LocalTensor<half> xLocal = inQueueX.AllocTensor<half>();
        LocalTensor<half> yLocal = inQueueY.AllocTensor<half>();
        DataCopy(xLocal, xGm, totalLength);
        DataCopy(yLocal, yGm, totalLength);
        inQueueX.EnQue(xLocal);
        inQueueY.EnQue(yLocal);

        // Compute: Vector Add
        xLocal = inQueueX.DeQue<half>();
        yLocal = inQueueY.DeQue<half>();
        LocalTensor<half> zLocal = outQueueZ.AllocTensor<half>();
        Add(zLocal, xLocal, yLocal, totalLength);
        outQueueZ.EnQue<half>(zLocal);

        // CopyOut: UB → GM
        zLocal = outQueueZ.DeQue<half>();
        DataCopy(zGm, zLocal, totalLength);
    }
    
private:
    TPipe pipe;
    TQue<QuePosition::VECIN, 1> inQueueX, inQueueY;
    TQue<QuePosition::VECOUT, 1> outQueueZ;
    GlobalTensor<half> xGm, yGm, zGm;
    uint32_t totalLength;
};
```

## Key API Categories

| Category | APIs | Purpose |
|----------|------|---------|
| Data Movement | DataCopy, DataCopyPad | GM ↔ UB transfer with optional padding |
| Vector Compute | Add, Mul, Sub, Div, ReduceSum, Max, Min | SIMD operations on Vector unit |
| Matrix Compute | Matmul (via Cube) | GEMM operations on Cube unit |
| Synchronization | PipeBarrier, SyncAll | Queue and cross-core synchronization |
| Memory Management | TPipe, TBuf, TQue | Unified Buffer allocation and management |

## Supported Data Types

- **Floating Point**: FP16, FP32, BF16
- **Integer**: INT8, INT32, UINT8

## Comparison with CUDA

| Concept | AscendC | CUDA C++ |
|---------|---------|----------|
| Kernel entry | `__aicore__ void Process()` | `__global__ void kernel()` |
| Programming model | Class-based with Init/Process | Function-based |
| Memory model | GM/UB/L0 (explicit queue-based) | Global/Shared/Register |
| Parallelism | Multi-core SPMD with tile-based processing | Grid/Block/Thread hierarchy |
| Synchronization | PipeBarrier between queue stages | __syncthreads() across threads |
| Vector operations | Explicit Add(), Mul() APIs | Element-wise operations per-thread |
| Matrix operations | Cube Matmul API (NZ format) | WMMA/MMA Tensor Core ops |

## Development Workflow

1. **Write kernel**: Create C++ class with Init() and Process() methods
2. **Compile**: Use AscendC compiler (aicll) to generate .o and .json files
3. **Register**: Add operator to .json registration file
4. **Build application**: Link with AscendCL runtime
5. **Execute**: Deploy to Ascend NPU via ACL APIs

## Performance Optimization Tips

- **Overlap compute and memory**: Use multiple queues to pipeline CopyIn/Compute/CopyOut
- **Tile size selection**: Match tile size to Vector/Cube unit capabilities (typically 32/64 for FP16)
- **NZ format**: Keep data in NZ format throughout pipeline to avoid transposes
- **Double buffering**: Allocate 2 buffers per queue to hide latency
- **Reduce GM access**: Maximize reuse in UB before copying back to GM
