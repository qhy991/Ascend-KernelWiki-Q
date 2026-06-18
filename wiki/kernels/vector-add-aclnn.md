---
id: kernel-vector-add-aclnn
title: "aclnn Vector Add — Single-Operator Invocation in C++"
type: wiki-kernel
architectures: [ascend910, ascend910b]
tags: [elementwise, aclnn, cpp, runtime]
confidence: source-reported
kernel_types: [elementwise]
languages: [cpp]
sources: [doc-aclnn-operator-api, blog-aclnn-custom-op-invocation, doc-ascendcl-runtime]
related: [lang-aclnn-cpp-guide, lang-ascendcl-host-guide, kernel-elementwise-ascendc]
reproducibility: snippet
---

# aclnn Vector Add — Single-Operator Invocation in C++

This page is the **host-side** counterpart to the device kernels in this collection. Where kernel-elementwise-ascendc *authors* an Add on the Vector unit, here we author **no device code at all** — we call the prebuilt `aclnnAdd` operator from CANN through the aclnn single-operator API and drive it end-to-end from regular host C++. The same flow applies verbatim to any other `aclnnXxx` operator; only the descriptor arguments and the symbol name change.

## What aclnn Gives You

aclnn (Ascend CL Neural Network) exposes each operator as a pair of C symbols: `aclnnXxxGetWorkspaceSize` and `aclnnXxx`. The host sizes a scratch workspace and builds an opaque executor in phase 1, then enqueues asynchronous execution in phase 2. The kernel itself — tiling, pipeline scheduling, Vector-unit dispatch — is already baked into the operator binary. See lang-aclnn-cpp-guide for the conceptual split between this *invocation layer* and the AscendC *authoring layer*, and lang-ascendcl-host-guide for the runtime primitives (`aclInit`, device, stream, memory) used below.

## End-to-End Flow

The complete `out = self + alpha * other` computation for two fp16 vectors breaks into six stages:

1. **Runtime init** — `aclInit`, `aclrtSetDevice`, `aclrtCreateStream`.
2. **Device memory + H2D** — `aclrtMalloc` three buffers, `aclrtMemcpy` the two inputs host→device.
3. **Descriptors** — wrap each device buffer in an `aclTensor` via `aclCreateTensor`, plus an `aclScalar` for `alpha`.
4. **Phase 1** — `aclnnAddGetWorkspaceSize(self, other, alpha, out, &workspaceSize, &executor)`; `aclrtMalloc` the workspace.
5. **Phase 2** — `aclnnAdd(workspace, workspaceSize, executor, stream)`; `aclrtSynchronizeStream`.
6. **D2H + teardown** — `aclrtMemcpy` the result device→host, then destroy descriptors and free buffers.

## Full Host Code

```cpp
#include "acl/acl.h"
#include "aclnnop/aclnn_add.h"
#include <vector>
#include <cstdint>

int main() {
    // ---- Stage 1: runtime initialization ----
    aclInit(nullptr);
    int32_t deviceId = 0;
    aclrtSetDevice(deviceId);
    aclrtStream stream = nullptr;
    aclrtCreateStream(&stream);

    // ---- Problem setup: out = self + alpha * other, fp16 length 8 ----
    const int64_t N = 8;
    int64_t shape[]   = {N};
    int64_t strides[] = {1};
    const size_t bytes = N * sizeof(uint16_t);  // fp16 == 2 bytes/elem

    std::vector<uint16_t> hSelf(N),  hOther(N),  hOut(N);
    // ... fill hSelf / hOther with fp16 bit patterns ...

    // ---- Stage 2: device memory + host->device copies ----
    void *selfDev = nullptr, *otherDev = nullptr, *outDev = nullptr;
    aclrtMalloc(&selfDev,  bytes, ACL_MEM_MALLOC_HUGE_FIRST);
    aclrtMalloc(&otherDev, bytes, ACL_MEM_MALLOC_HUGE_FIRST);
    aclrtMalloc(&outDev,   bytes, ACL_MEM_MALLOC_HUGE_FIRST);

    aclrtMemcpy(selfDev,  bytes, hSelf.data(),  bytes, ACL_MEMCPY_HOST_TO_DEVICE);
    aclrtMemcpy(otherDev, bytes, hOther.data(), bytes, ACL_MEMCPY_HOST_TO_DEVICE);

    // ---- Stage 3: descriptors (aclTensor per buffer, aclScalar for alpha) ----
    aclTensor* self  = aclCreateTensor(shape, 1, ACL_FLOAT16, strides, 0,
                                       ACL_FORMAT_ND, shape, 1, selfDev);
    aclTensor* other = aclCreateTensor(shape, 1, ACL_FLOAT16, strides, 0,
                                       ACL_FORMAT_ND, shape, 1, otherDev);
    aclTensor* out   = aclCreateTensor(shape, 1, ACL_FLOAT16, strides, 0,
                                       ACL_FORMAT_ND, shape, 1, outDev);

    float alphaVal = 1.0f;
    aclScalar* alpha = aclCreateScalar(&alphaVal, ACL_FLOAT);

    // ---- Stage 4: phase 1 — size workspace, build executor ----
    uint64_t workspaceSize = 0;
    aclOpExecutor* executor = nullptr;
    aclnnAddGetWorkspaceSize(self, other, alpha, out,
                             &workspaceSize, &executor);

    void* workspace = nullptr;
    if (workspaceSize > 0) {
        aclrtMalloc(&workspace, workspaceSize, ACL_MEM_MALLOC_HUGE_FIRST);
    }

    // ---- Stage 5: phase 2 — enqueue and wait ----
    aclnnAdd(workspace, workspaceSize, executor, stream);
    aclrtSynchronizeStream(stream);

    // ---- Stage 6: device->host result + teardown ----
    aclrtMemcpy(hOut.data(), bytes, outDev, bytes, ACL_MEMCPY_DEVICE_TO_HOST);
    // ... hOut now holds the fp16 sum ...

    if (workspace) aclrtFree(workspace);
    aclDestroyScalar(alpha);
    aclDestroyTensor(self);
    aclDestroyTensor(other);
    aclDestroyTensor(out);
    aclrtFree(selfDev);
    aclrtFree(otherDev);
    aclrtFree(outDev);

    aclrtDestroyStream(stream);
    aclrtResetDevice(deviceId);
    aclFinalize();
    return 0;
}
```

## Anatomy of the Two-Phase Call

The `aclnnAdd` signature mirrors the PyTorch-style `add`: it computes `out = self + alpha * other`, where `alpha` is an `aclScalar` (here `1.0f`, i.e. a plain sum). Phase 1 inspects the input/output descriptors and the attribute to determine the scratch `workspaceSize` and to construct the `aclOpExecutor`. Phase 2 consumes that executor with the just-allocated workspace pointer and the stream. The split is what lets the host allocate device workspace deterministically before any kernel launches.

| Argument | Phase 1 `GetWorkspaceSize` | Phase 2 `aclnnAdd` |
|----------|----------------------------|--------------------|
| `self`, `other` | input `aclTensor*` | — (captured by executor) |
| `alpha` | input `aclScalar*` | — |
| `out` | output `aclTensor*` | — |
| `workspaceSize` | `uint64_t*` (out) | `uint64_t` (in) |
| `executor` | `aclOpExecutor**` (out) | `aclOpExecutor*` (in) |
| `workspace` | — | `void*` device ptr |
| `stream` | — | `aclrtStream` |

## The Same Pattern for Any aclnn Op

Nothing in stages 1, 2, 5, and 6 is Add-specific. To call a different operator you change only:

- the include (`aclnnop/aclnn_<op>.h`),
- the per-op descriptor arguments to `aclnn<Op>GetWorkspaceSize(...)`,
- the symbol pair `aclnn<Op>GetWorkspaceSize` / `aclnn<Op>`.

A **custom** operator authored in AscendC and installed via the `msopgen` toolchain (covered in lang-aclnn-cpp-guide) exports exactly this two-phase shape, so it is invoked through the identical six-stage host flow — the call site cannot tell a custom op from a CANN built-in.

## Trade-offs, Pitfalls, and Notes

- **Phase order is mandatory.** The `executor` is bound to its `GetWorkspaceSize` call; invoking `aclnnAdd` with a stale or mismatched executor is undefined behavior.
- **Workspace may be zero.** Many element-wise ops report `workspaceSize == 0`. Guard the `aclrtMalloc` (as above) so you do not request a zero-byte buffer, and pass `nullptr`/`0` to `aclnnAdd` in that case.
- **Descriptor vs. buffer lifetime.** `aclDestroyTensor` frees only the descriptor; you must still `aclrtFree` the underlying device buffer or you leak device memory.
- **Format must match the op.** `aclCreateTensor` here uses `ACL_FORMAT_ND` with explicit `strides`; supplying a format the operator does not expect (e.g. `ACL_FORMAT_NZ`) can trigger an internal layout conversion or wrong results.
- **Execution is asynchronous.** `aclnnAdd` only enqueues work on the `stream`; the D2H copy result is valid only after `aclrtSynchronizeStream` returns.
- **Author vs. invoke.** If no built-in or installed operator does what you need, aclnn cannot express it — you must author an AscendC kernel (see kernel-elementwise-ascendc and lang-aclnn-cpp-guide) and install it before aclnn can reach it.

## When To Use This Path

Reach for aclnn when an operator already exists and you simply need to run it one call at a time from host C++ — model glue, validation harnesses, or single-op micro-benchmarks. For authoring new device behavior, write the AscendC kernel instead (kernel-elementwise-ascendc); for the runtime scaffolding every aclnn call depends on, see lang-ascendcl-host-guide.
