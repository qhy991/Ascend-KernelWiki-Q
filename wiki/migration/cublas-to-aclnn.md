---
id: migration-cublas-to-aclnn
title: "cuBLAS / cuDNN -> aclnn — Library-Call Operator Migration"
type: wiki-migration
tags: [cublas, cudnn, aclnn, migration, operator]
confidence: source-reported
sources: [doc-aclnn-operator-api, doc-catlass-framework, doc-ascendc-api-reference]
from_concept: "cuBLAS / cuDNN library calls"
to_concept: "aclnn single-operator API"
difficulty: moderate
related: [lang-aclnn-cpp-guide, migration-cutlass-to-catlass, kernel-vector-add-aclnn]
---

Most production GPU code never writes a kernel — it calls a vendor library. `cublasSgemm`, `cudnnConvolutionForward`, and `cudnnSoftmaxForward` cover the bulk of inference and training math. On Ascend the equivalent layer is **aclnn** (Ascend CANN Library of Neural Networks), a catalog of single-operator entry points reached through AscendCL. This guide maps the common cuBLAS/cuDNN calls onto their aclnn counterparts and explains the one structural change you cannot avoid: the **two-phase calling convention**.

## Operator Mapping Table

| cuBLAS / cuDNN call | aclnn equivalent | Notes |
|---------------------|------------------|-------|
| `cublasSgemm` / `cublasGemmEx` | `aclnnMatmul` (or `aclnnGemm`) | `aclnnGemm` exposes alpha/beta + bias; `aclnnMatmul` is the plain `C = A·B` form |
| `cublasGemmStridedBatchedEx` | `aclnnBatchMatMul` | Batched GEMM; batch dim is leading dim of ND tensor |
| `cudnnConvolutionForward` | `aclnnConvolution` | Covers 1D/2D/3D conv via the `stride`/`padding`/`dilation` arrays |
| `cudnnSoftmaxForward` | `aclnnSoftmax` | `dim` argument replaces cuDNN's mode/algorithm enums |
| `cudnnBatchNormalizationForward*` | `aclnnBatchNorm` | Running-stats vs training mode selected by argument, not a separate handle |
| LayerNorm (cuDNN frontend / custom) | `aclnnLayerNorm` | Returns `out`, `meanOut`, `rstdOut` |
| RMSNorm (custom CUDA) | `aclnnRmsNorm` | Native operator; no cuDNN analogue |
| Attention (FlashAttention CUDA) | `aclnnFlashAttentionScore` | Fused QK^T · softmax · V; replaces hand-rolled flash kernels |

The mapping is mostly one-to-one at the *semantic* level. The friction is entirely in how the call is issued.

## The Core Difference: Handle+Call vs Two-Phase Execute

cuBLAS uses a stateful **handle** and a single blocking-style call. The library owns its own scratch memory internally, so you never see a workspace.

aclnn splits every operator into **two phases**:

1. **`aclnn<Op>GetWorkspaceSize(...)`** — validates shapes/dtypes, plans the tiling, and reports how many bytes of device scratch the operator needs plus an opaque **executor** handle.
2. **`aclnn<Op>(...)`** — runs the planned executor on a stream using a workspace *you* allocated.

You allocate the workspace yourself (via `aclrtMalloc`) between the two phases. Tensors are not raw pointers either: each operand is wrapped in an `aclTensor` built with **`aclCreateTensor`**, which carries shape, dtype, **ND** format, and stride.

| Aspect | cuBLAS / cuDNN | aclnn |
|--------|----------------|-------|
| Context | `cublasHandle_t` / `cudnnHandle_t` | none — stream-scoped executor |
| Operands | raw device pointers + descriptors | `aclTensor` via `aclCreateTensor` |
| Scratch memory | hidden inside the library | explicit workspace you `aclrtMalloc` |
| Call shape | one call | `GetWorkspaceSize` then execute |
| Default layout | **column-major** (Fortran) | **ND** (row-major, natural) |

### Layout gotcha: column-major vs ND

cuBLAS is column-major. A huge amount of CUDA code "transposes by swapping" — computing `C^T = B^T · A^T` so column-major math produces a row-major result. aclnn `aclTensor`s are **ND** (row-major / natural order), so when you port `cublasSgemm` you drop the transpose trickery: pass A, B, C in their natural row-major shapes and set the transpose flags (or the `aclnnMatmul` operand order) to match the *math* you actually want, not the layout workaround.

## Before / After: SGEMM

### Before — cuBLAS (column-major, single call)

```cpp
// C = A * B, all in column-major device memory
cublasHandle_t handle;
cublasCreate(&handle);
const float alpha = 1.0f, beta = 0.0f;
cublasSgemm(handle,
            CUBLAS_OP_N, CUBLAS_OP_N,
            m, n, k,
            &alpha,
            dA, /*lda=*/m,
            dB, /*ldb=*/k,
            &beta,
            dC, /*ldc=*/m);
cublasDestroy(handle);
```

### After — aclnn (ND tensors, two-phase execute)

```cpp
// 1. Wrap operands as ND aclTensors (row-major shapes [m,k], [k,n], [m,n])
aclTensor *a = aclCreateTensor(shapeA, 2, ACL_FLOAT, strideA, 0,
                               ACL_FORMAT_ND, shapeA, 2, dA);
aclTensor *b = aclCreateTensor(shapeB, 2, ACL_FLOAT, strideB, 0,
                               ACL_FORMAT_ND, shapeB, 2, dB);
aclTensor *out = aclCreateTensor(shapeC, 2, ACL_FLOAT, strideC, 0,
                                 ACL_FORMAT_ND, shapeC, 2, dC);

// 2. Phase 1 — plan: returns workspace size + executor
uint64_t workspaceSize = 0;
aclOpExecutor *executor = nullptr;
int8_t cubeMathType = 1;  // e.g. allow fp16/bf16 accumulation policy
aclnnMatmulGetWorkspaceSize(a, b, out, cubeMathType,
                            &workspaceSize, &executor);

// 3. Allocate the scratch the planner asked for
void *workspace = nullptr;
if (workspaceSize > 0) {
    aclrtMalloc(&workspace, workspaceSize, ACL_MEM_MALLOC_HUGE_FIRST);
}

// 4. Phase 2 — execute on the stream
aclnnMatmul(workspace, workspaceSize, executor, stream);
aclrtSynchronizeStream(stream);

// 5. Release
aclDestroyTensor(a); aclDestroyTensor(b); aclDestroyTensor(out);
if (workspace) aclrtFree(workspace);
```

The same `GetWorkspaceSize` → `aclrtMalloc` → execute rhythm holds for **every** aclnn operator — `aclnnConvolution`, `aclnnSoftmax`, `aclnnLayerNorm`, `aclnnRmsNorm`, and `aclnnFlashAttentionScore` all follow it. Once you have written the helper once, porting the next operator is mechanical. See `lang-aclnn-cpp-guide` for a reusable two-phase wrapper.

## Migration Workflow

1. **Inventory the library calls** — list every `cublas*` / `cudnn*` call site; each maps to one aclnn operator from the table above.
2. **Replace handles with streams** — drop `cublasCreate`/`cudnnCreate`; aclnn binds to an `aclrtStream`.
3. **Wrap operands** — build an `aclTensor` per operand with `aclCreateTensor`, declaring shape/dtype/`ACL_FORMAT_ND`/stride.
4. **Fix the layout** — remove column-major transpose workarounds; pass natural row-major shapes.
5. **Split each call in two** — call `aclnn<Op>GetWorkspaceSize`, `aclrtMalloc` the reported bytes, then call `aclnn<Op>`.
6. **Manage lifetime** — `aclDestroyTensor` each operand and `aclrtFree` the workspace; reuse a pooled workspace buffer across calls to avoid per-call malloc.
7. **Validate** — compare against the original cuBLAS/cuDNN output on small shapes before scaling up.

## When to Drop Below aclnn — CATLASS

aclnn is a fixed catalog: you get the operator the library author tiled, with the fusion and accumulation policy they chose. That is fine for standard inference shapes. It is *not* enough when you need:

- a **custom-tiled GEMM** (unusual M/N/K, a tile shape aclnn does not pick well, or a non-standard accumulation/quant path), or
- an **epilogue fusion** aclnn does not expose (bias + activation + cast folded into the GEMM tail).

In those cases drop to **CATLASS**, Ascend's CUTLASS-analogous template framework for hand-tiled GEMM on the Cube unit. That is the same boundary CUDA developers hit when `cublas` is not flexible enough and they reach for CUTLASS. The translation of CUTLASS tile/epilogue concepts to CATLASS is covered in `migration-cutlass-to-catlass`; for an end-to-end aclnn single-operator example see `kernel-vector-add-aclnn`.

```
                  ┌─────────────────────────────────────┐
  standard op  →  │  aclnn (aclnnMatmul / aclnnConv ...) │   call a library
                  └─────────────────────────────────────┘
                  ┌─────────────────────────────────────┐
  custom tile  →  │  CATLASS (templated Cube GEMM)       │   own the tiling
                  └─────────────────────────────────────┘
                  ┌─────────────────────────────────────┐
  full control →  │  AscendC kernel                      │   write the kernel
                  └─────────────────────────────────────┘
```

## Trade-offs, Pitfalls, and Notes

- **Workspace lifetime.** The executor and the workspace size are produced together in phase 1 and must be passed *as a pair* to phase 2. Do not call `GetWorkspaceSize` for operator A and execute with operator B's executor.
- **Reuse the workspace.** Allocating a fresh `aclrtMalloc` per call in a hot loop is a classic regression — pool one buffer sized to the max workspace seen.
- **Format is ND, not NZ.** aclnn operators accept **ND** `aclTensor`s and convert to the Cube-friendly NZ fractal format internally. You do *not* manually NZ-convert at the aclnn layer — that explicit NZ handling only resurfaces if you drop to CATLASS or a raw AscendC kernel.
- **dtype / `cubeMathType` policy.** `aclnnMatmul` takes a `cubeMathType` argument controlling the accumulation/precision policy; it replaces cuBLAS's compute-type enum (`cublasGemmEx`'s `computeType`). Pick it deliberately when matching numerical behavior.
- **Attention is fused.** A hand-written CUDA FlashAttention loop collapses into a single `aclnnFlashAttentionScore` call — do not port the tiled inner loop; port the *interface* (Q, K, V, mask, scale) and let the operator own the fusion.
- **No silent column-major.** The single most common correctness bug in this migration is leaving a cuBLAS-era transpose workaround in place against an ND tensor. Validate the first ported GEMM against a reference before trusting the rest.

## Related Resources

- [aclnn C++ guide](lang-aclnn-cpp-guide) — the two-phase calling pattern and a reusable wrapper
- [CUTLASS to CATLASS](migration-cutlass-to-catlass) — when a library call is not enough and you need custom Cube tiling
- [aclnn vector add example](kernel-vector-add-aclnn) — minimal end-to-end single-operator walkthrough
