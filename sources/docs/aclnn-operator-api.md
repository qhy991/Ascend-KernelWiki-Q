---
id: doc-aclnn-operator-api
title: "aclnn Single-Operator API Reference (Two-Phase Interface)"
type: source-doc
architectures: [ascend910, ascend910b, ascend310p]
tags: [aclnn, cpp, operator, cann, api]
date: '2026-02-20'
url: https://www.hiascend.com/document/detail/en/canncommercial/800/inferapplicationdev/aclcppdevg/aclcppdevg_0001.html
hardware_features: [global-memory, cube-unit, vector-unit]
confidence: verified
---

The aclnn (Ascend Operator Library) interface is the host-side C++ API in CANN for invoking single neural-network operators directly, without going through a graph executor or framework. Every operator exposes a uniform **two-phase** calling convention: a `GetWorkspaceSize` phase that plans the execution and reports how much scratch device memory is required, followed by an execution phase that launches the operator asynchronously on an `aclrtStream`. This page documents that convention as the canonical way to call fused and primitive operators such as `aclnnMatmul`, `aclnnAdd`, `aclnnFlashAttentionScore`, and `aclnnRmsNorm`.

## The Two-Phase Interface

Each operator `Xxx` ships as a pair of functions. The pattern is rigid and identical across the library, which is what makes the API composable:

```cpp
// Phase 1 — planning: compute required workspace and build an executor.
aclnnStatus aclnnXxxGetWorkspaceSize(
    const aclTensor* input,      // input tensors (one or more)
    /* ... more inputs ... */
    aclTensor*       out,        // output tensor(s)
    uint64_t*        workspaceSize, // [out] required scratch bytes
    aclOpExecutor**  executor);  // [out] opaque, reusable plan handle

// Phase 2 — execution: run the operator asynchronously on a stream.
aclnnStatus aclnnXxx(
    void*          workspace,     // device buffer of >= workspaceSize bytes
    uint64_t       workspaceSize, // value returned by phase 1
    aclOpExecutor* executor,      // handle returned by phase 1
    aclrtStream    stream);       // execution stream
```

Both functions return an `aclnnStatus` (`ACLNN_SUCCESS == 0` on success). The split exists because the library cannot know the scratch requirement until it has inspected the concrete tensor shapes, dtypes, and formats. Phase 1 performs that analysis once and packs the resulting plan into the `aclOpExecutor`; phase 2 is then a thin, cheap dispatch that the host can issue repeatedly.

### Why split planning from execution

- **Caller-owned workspace**: the library never allocates device scratch implicitly. You allocate it with `aclrtMalloc` *after* phase 1 tells you the size, so memory ownership and lifetime are explicit and poolable.
- **Asynchronous launch**: phase 2 only enqueues work on `stream` and returns immediately, so it overlaps cleanly with other streams (see `doc-ascend-multi-stream-guide`).
- **Plan reuse**: the `executor` encodes the tiling/algorithm choice and can be reused across launches with identical shapes, amortizing planning cost.

## Building Tensors

Operators consume `aclTensor` descriptors that wrap an existing device address. Tensors are created with `aclCreateTensor` and released with `aclDestroyTensor`:

```cpp
// View shape vs. underlying storage shape are described separately,
// which lets aclTensor express slices, transposes, and padded layouts.
aclTensor* aclCreateTensor(
    const int64_t* viewDims,     // logical shape seen by the operator
    uint64_t       viewDimsNum,
    aclDataType    dataType,     // ACL_FLOAT16, ACL_BF16, ACL_INT8, ...
    const int64_t* strides,      // element strides for the view
    int64_t        offset,       // element offset into storage
    aclFormat      format,       // ACL_FORMAT_ND, ACL_FORMAT_FRACTAL_NZ, ...
    const int64_t* storageDims,  // physical shape of the backing buffer
    uint64_t       storageDimsNum,
    void*          deviceAddr);  // base device pointer (from aclrtMalloc)

void aclDestroyTensor(const aclTensor* tensor);
```

The separation of `viewDims`/`strides`/`offset` from `storageDims` is what allows a single device buffer to be presented as a transposed or sliced operand without copying. Note that `format` may be `ACL_FORMAT_FRACTAL_NZ` for Cube-bound operands; the NZ layout matters for matmul-class kernels (see `kernel-matmul-ascendc` and the NZ tiling discussion in `technique-nz-tiling`).

## End-to-End Call Sequence

A complete single-operator invocation threads the two phases together with explicit workspace allocation:

```cpp
// 0. Inputs/outputs already live in device memory (aclrtMalloc'd) and are
//    wrapped as aclTensor* (self, other, out) via aclCreateTensor.

// 1. PLAN: ask the operator how much workspace it needs.
uint64_t       workspaceSize = 0;
aclOpExecutor* executor      = nullptr;
aclnnStatus ret = aclnnAddGetWorkspaceSize(
    self, other, /*alpha=*/one, out, &workspaceSize, &executor);
// check ret == ACLNN_SUCCESS

// 2. ALLOCATE: caller owns the scratch buffer.
void* workspace = nullptr;
if (workspaceSize > 0) {
    aclrtMalloc(&workspace, workspaceSize, ACL_MEM_MALLOC_HUGE_FIRST);
}

// 3. EXECUTE: enqueue asynchronously on the stream.
ret = aclnnAdd(workspace, workspaceSize, executor, stream);
// check ret == ACLNN_SUCCESS

// 4. SYNC + CLEANUP.
aclrtSynchronizeStream(stream);
if (workspace) aclrtFree(workspace);
aclDestroyTensor(self);
aclDestroyTensor(other);
aclDestroyTensor(out);
```

The same skeleton applies verbatim to every operator — only the tensor arguments to the `GetWorkspaceSize` call change. For `aclnnMatmul` you pass the two operand tensors and the result tensor; for `aclnnFlashAttentionScore` you pass query/key/value plus the various mask and scale arguments; for `aclnnRmsNorm` you pass the input, the gamma weight, and an epsilon.

## Operator Coverage

aclnn is part of the CANN Ascend Operator Library and spans both primitive and fused operators, so common transformer building blocks are available as single calls rather than hand-written kernels:

| Operator               | Category    | Typical use                              |
| ---------------------- | ----------- | ---------------------------------------- |
| `aclnnAdd`             | elementwise | residual / bias add on the Vector unit   |
| `aclnnMatmul`          | matmul      | dense GEMM on the Cube unit              |
| `aclnnRmsNorm`         | norm        | pre-norm in LLM transformer blocks       |
| `aclnnFlashAttentionScore` | fused attention | memory-efficient attention in one op |

Because the fused operators (e.g. `aclnnFlashAttentionScore`) collapse multiple stages into a single launch, they avoid intermediate round-trips to global memory in the same spirit as the hand-fused kernels in `doc-ascend-operator-fusion`. When an aclnn operator does not exist or does not fit, the alternative is writing a custom kernel with the AscendC API (`doc-ascendc-api-reference`).

## Trade-offs, Pitfalls, and Notes

- **Never skip phase 1.** The `workspaceSize` and `executor` from `GetWorkspaceSize` are mandatory inputs to the execution call. Calling `aclnnXxx` with a stale or null `executor`, or with a workspace smaller than the reported size, is undefined behavior.
- **Workspace can be zero.** Many elementwise operators report `workspaceSize == 0`; guard the `aclrtMalloc` so you do not allocate a zero-byte buffer, and pass `nullptr` for `workspace` in that case.
- **Executor lifetime is single-shot by default.** The `aclOpExecutor` returned by phase 1 is consumed by the matching phase-2 call. Re-plan (re-run phase 1) for a new launch unless you have explicitly opted into executor reuse for identical shapes.
- **Async means you must synchronize.** `aclnnXxx` returns before the kernel completes; results are not valid until `aclrtSynchronizeStream` (or an event wait) confirms completion. This is what enables multi-stream overlap, but it also means premature device-to-host copies will read garbage.
- **Tensor descriptors are not buffers.** `aclCreateTensor` only describes existing device memory; it does not allocate or copy. Free the `aclTensor` with `aclDestroyTensor`, and free the underlying `deviceAddr` separately with `aclrtFree`.
- **Format must match the operand role.** Cube-bound operands frequently expect `ACL_FORMAT_FRACTAL_NZ`; passing `ACL_FORMAT_ND` where NZ is required forces an internal conversion (extra workspace and latency) or an error.

## Related Pages

- `doc-ascendc-api-reference` — write a custom kernel when no aclnn operator fits.
- `doc-ascend-multi-stream-guide` — overlap asynchronous aclnn launches across streams.
- `doc-ascend-operator-fusion` — fused aclnn ops mirror these hand-fusion patterns.
- `kernel-matmul-ascendc` — Cube-unit matmul behind `aclnnMatmul`.
- `technique-nz-tiling` — NZ format expected by Cube-bound aclnn operands.
