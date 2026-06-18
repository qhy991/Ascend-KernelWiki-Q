---
id: blog-aclnn-custom-op-invocation
title: "Calling a Custom aclnn Operator from C++ — End to End"
type: source-blog
author: ascend-developer
date: '2026-01-18'
url: https://developer.aliyun.com/article/1643991
architectures: [ascend910, ascend910b]
tags: [aclnn, cpp, operator, runtime, tutorial]
hardware_features: [global-memory]
kernel_types: [elementwise]
languages: [cpp]
confidence: source-reported
---

Once you have built a custom Ascend operator with the `op_host`/`op_kernel` project layout, the next question is always the same: how do I actually call it from a host program? This tutorial walks the complete C++ flow for invoking a custom `aclnn` operator through the AscendCL runtime, from `aclInit` to teardown, using the two-phase `GetWorkspaceSize` / execute interface that every `aclnn` operator exposes.

## Background: Where the aclnn Symbol Comes From

When you scaffold an operator with `msopgen` and implement the host tiling in `op_host/` and the kernel in `op_kernel/`, the build produces a custom operator package — a self-extracting `custom_opp_<os>_<arch>.run` file. Installing that package registers the operator and, crucially, exposes two C symbols per operator:

- `aclnnXxxGetWorkspaceSize(...)` — phase 1, computes the workspace requirement and builds an executor handle.
- `aclnnXxx(...)` — phase 2, launches the kernel on a stream.

These symbols are linked from the custom operator library that ships inside the run package. Without installing `custom_opp_*.run`, the linker cannot resolve `aclnnXxx` and your host program will fail to build or load. This is the single most common stumbling block, so it is worth stating up front: **install the run package first**, then compile against it.

## The Two-Phase aclnn Interface

Every `aclnn` operator follows the same calling convention:

1. **Workspace query** — `aclnnXxxGetWorkspaceSize` takes the input/output tensor descriptors plus operator attributes, and returns (a) the number of workspace bytes the kernel needs and (b) an opaque `aclOpExecutor*` handle that caches the planned execution.
2. **Execution** — `aclnnXxx` takes the allocated workspace, its size, the same executor handle, and the stream to launch on.

This split lets the runtime plan tiling once and reuse it, and it means you always perform **two** `aclrtMalloc` calls: one for the operator's data buffers and one for the workspace.

## Full Host Flow

The skeleton below shows a complete invocation of a custom element-wise operator (here named `Xxx`, e.g. an `Add`-style op) on a single device. Error handling is condensed to a `CHECK` macro for readability.

```cpp
#include <vector>
#include "acl/acl.h"
#include "aclnn_xxx.h"   // generated header from the custom op package

#define CHECK(expr) do { aclError _e = (expr); if (_e != ACL_SUCCESS) return _e; } while (0)

int RunCustomOp() {
    // 1. Initialize AscendCL and select a device + stream
    CHECK(aclInit(nullptr));
    CHECK(aclrtSetDevice(0));
    aclrtStream stream = nullptr;
    CHECK(aclrtCreateStream(&stream));

    // 2. Host data
    std::vector<int64_t> shape = {8, 2048};
    size_t elemCount = 8 * 2048;
    size_t byteSize  = elemCount * sizeof(float);
    std::vector<float> hostX(elemCount, 1.0f);
    std::vector<float> hostY(elemCount, 2.0f);
    std::vector<float> hostOut(elemCount, 0.0f);

    // 3. Allocate device buffers (data malloc #1)
    void *devX = nullptr, *devY = nullptr, *devOut = nullptr;
    CHECK(aclrtMalloc(&devX,   byteSize, ACL_MEM_MALLOC_HUGE_FIRST));
    CHECK(aclrtMalloc(&devY,   byteSize, ACL_MEM_MALLOC_HUGE_FIRST));
    CHECK(aclrtMalloc(&devOut, byteSize, ACL_MEM_MALLOC_HUGE_FIRST));

    // 4. Copy inputs Host -> Device
    CHECK(aclrtMemcpy(devX, byteSize, hostX.data(), byteSize, ACL_MEMCPY_HOST_TO_DEVICE));
    CHECK(aclrtMemcpy(devY, byteSize, hostY.data(), byteSize, ACL_MEMCPY_HOST_TO_DEVICE));

    // 5. Wrap device buffers as aclTensor (ND layout for an elementwise op)
    aclTensor *tX = aclCreateTensor(shape.data(), shape.size(), ACL_FLOAT,
                                    nullptr, 0, ACL_FORMAT_ND,
                                    shape.data(), shape.size(), devX);
    aclTensor *tY = aclCreateTensor(shape.data(), shape.size(), ACL_FLOAT,
                                    nullptr, 0, ACL_FORMAT_ND,
                                    shape.data(), shape.size(), devY);
    aclTensor *tOut = aclCreateTensor(shape.data(), shape.size(), ACL_FLOAT,
                                      nullptr, 0, ACL_FORMAT_ND,
                                      shape.data(), shape.size(), devOut);

    // 6. Phase 1 — query workspace size and build the executor
    uint64_t workspaceSize = 0;
    aclOpExecutor *executor = nullptr;
    CHECK(aclnnXxxGetWorkspaceSize(tX, tY, tOut, &workspaceSize, &executor));

    // 7. Allocate workspace (data malloc #2) — only if the op needs it
    void *workspace = nullptr;
    if (workspaceSize > 0) {
        CHECK(aclrtMalloc(&workspace, workspaceSize, ACL_MEM_MALLOC_HUGE_FIRST));
    }

    // 8. Phase 2 — launch the kernel on the stream
    CHECK(aclnnXxx(workspace, workspaceSize, executor, stream));

    // 9. Wait for completion
    CHECK(aclrtSynchronizeStream(stream));

    // 10. Copy result Device -> Host
    CHECK(aclrtMemcpy(hostOut.data(), byteSize, devOut, byteSize, ACL_MEMCPY_DEVICE_TO_HOST));

    // 11. Teardown — destroy tensors, free buffers, release runtime
    aclDestroyTensor(tX);
    aclDestroyTensor(tY);
    aclDestroyTensor(tOut);
    if (workspace) aclrtFree(workspace);
    aclrtFree(devX);
    aclrtFree(devY);
    aclrtFree(devOut);
    aclrtDestroyStream(stream);
    CHECK(aclrtResetDevice(0));
    CHECK(aclFinalize());
    return ACL_SUCCESS;
}
```

## Flow Summary

The lifecycle is strictly ordered. Skipping or reordering steps (for example, creating a tensor before the device is set) produces runtime errors that are hard to diagnose.

| Step | API | Purpose |
|------|-----|---------|
| Init | `aclInit` | Bring up the AscendCL runtime |
| Device | `aclrtSetDevice` | Bind the calling thread to a device |
| Stream | `aclrtCreateStream` | Create the execution queue |
| Data alloc | `aclrtMalloc` (#1) | Device buffers for inputs/output |
| Upload | `aclrtMemcpy` H2D | Stage inputs on the device |
| Describe | `aclCreateTensor` | Wrap buffers as typed/shaped tensors |
| Plan | `aclnnXxxGetWorkspaceSize` | Get workspace size + executor handle |
| WS alloc | `aclrtMalloc` (#2) | Workspace scratch buffer |
| Launch | `aclnnXxx` | Enqueue the kernel on the stream |
| Sync | `aclrtSynchronizeStream` | Block until the kernel finishes |
| Download | `aclrtMemcpy` D2H | Read results back to host |
| Teardown | `aclDestroyTensor` / `aclrtFree` | Release all resources |

## Packaging Notes: Making `aclnnXxx` Linkable

The generated header `aclnn_xxx.h` and the matching symbols live inside the custom operator package, not in base CANN. The typical sequence is:

1. Scaffold with `msopgen` from the operator prototype definition.
2. Implement `op_host/` (tiling, shape inference) and `op_kernel/` (the AscendC compute).
3. Build the project to produce `custom_opp_<os>_<arch>.run`.
4. Run the `.run` installer; it deploys the op into the vendor operator directory and registers the `aclnn` symbols.
5. Compile the host program against the installed package, linking the custom op library so `aclnnXxxGetWorkspaceSize` / `aclnnXxx` resolve.

If you change the operator signature, rebuild and reinstall the run package — a stale install will give you a header that no longer matches the linked symbol.

## Pitfalls and Notes

- **Two mallocs, always.** One for data buffers, one for workspace. A `workspaceSize` of `0` is valid for trivial element-wise ops; guard the second `aclrtMalloc` with an `if`.
- **Executor is single-use per plan.** The `aclOpExecutor*` returned by `GetWorkspaceSize` is consumed by the paired `aclnnXxx` call. Do not reuse a handle across launches; re-query for each new shape.
- **Format must match the operator.** This example uses `ACL_FORMAT_ND`, which is correct for element-wise operators. Cube-bound operators expect the 5D NZ layout instead — see `blog-nz-format-explained` for why, and `kernel-matmul-ascendc` for an NZ-formatted matmul.
- **Synchronize before D2H.** `aclnnXxx` only enqueues work; the output buffer is not valid until `aclrtSynchronizeStream` returns. Reading back too early yields stale data.
- **Tensor lifetime.** `aclCreateTensor` does not own the device memory — it only describes it. Free the underlying buffer with `aclrtFree` *after* `aclDestroyTensor`, and never the other way around.
- **Package must be installed.** A link error on `aclnnXxx` almost always means the `custom_opp_*.run` package was not installed in the active CANN environment.

## Related Pages

- [NZ format explainer](blog-nz-format-explained) — when ND is not enough for Cube-bound ops
- [AscendC programming guide](blog-ascendc-programming-guide) — the kernel side that backs the operator
- [Matmul kernel in AscendC](kernel-matmul-ascendc) — a Cube operator that uses the NZ format path
