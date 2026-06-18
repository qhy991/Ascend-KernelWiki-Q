---
id: lang-aclnn-cpp-guide
title: "aclnn — C++ Single-Operator API and Custom Operators"
type: wiki-language
tags: [aclnn, cpp, operator, runtime]
confidence: source-reported
sources: [doc-aclnn-operator-api, blog-aclnn-custom-op-invocation, doc-ascendcl-runtime]
architectures: [ascend910, ascend910b, ascend310p]
languages: [cpp]
related: [lang-ascendcl-host-guide, lang-ascendc-guide, kernel-vector-add-aclnn]
---

## Overview

aclnn (Ascend CL Neural Network) is the C++ single-operator API that lets host code invoke a single, prebuilt operator on the Ascend NPU without writing any device-side kernel code. It sits on top of the AscendCL runtime as an **invocation layer**: where AscendC (see lang-ascendc-guide) is the **authoring layer** in which you write the device kernel, aclnn is the layer where you *call* an operator that already exists in the operator package. Each operator is exposed as a pair of C symbols — `aclnnXxxGetWorkspaceSize` and `aclnnXxx` — and you drive both from regular host C++.

## aclnn vs. Authoring an AscendC Kernel

| Aspect | aclnn (this page) | AscendC kernel (lang-ascendc-guide) |
|--------|-------------------|-------------------------------------|
| Role | Invocation layer (caller) | Authoring layer (author) |
| What you write | Host C++ that calls `aclnnXxx` | Device C++ class with `Init()`/`Process()` |
| Where code runs | Host (CPU), dispatches to NPU | AICore (NPU) |
| Tiling / scheduling | Already baked into the op | You write it yourself |
| Typical use | Use an existing/built op as a black box | Implement new device behavior |
| Built artifact | Linked `.so` of the op package | `.o` kernel registered into the op package |

In short: AscendC produces an operator binary; aclnn consumes it. A custom AscendC operator, once built and installed, is callable through exactly the same two-phase aclnn interface as the built-in operators shipped with CANN.

## The Two-Phase Interface

Every aclnn operator follows the same two-call contract. You must call the workspace-sizing function first, allocate that workspace on the device, then execute.

1. **Phase 1 — `aclnnXxxGetWorkspaceSize(...)`**: Pass the input/output `aclTensor` handles plus any attributes. It computes the required scratch workspace size and produces an opaque executor handle (`aclOpExecutor*`). No computation happens yet.
2. **Phase 2 — `aclnnXxx(workspace, workspaceSize, executor, stream)`**: Pass the workspace device pointer, its size, the executor from phase 1, and an `aclrtStream`. This enqueues the operator for asynchronous execution on the stream.

The split exists so the host can size and allocate device workspace deterministically before launch, and so the executor can be reused across the matched `GetWorkspaceSize`/execute pair.

## aclTensor Creation and Destruction

aclnn does not consume raw device pointers directly — it consumes `aclTensor` descriptors that wrap a device buffer together with shape, dtype, strides, and data format. The lifecycle is:

- Allocate device memory with `aclrtMalloc` (runtime setup is covered in lang-ascendcl-host-guide).
- Build a descriptor with `aclCreateTensor`, passing the shape array, dtype (e.g. `ACL_FLOAT16`), format (e.g. `ACL_FORMAT_ND`), stride array, offset, and the device data pointer.
- After execution and stream synchronization, release each descriptor with `aclDestroyTensor` and free the underlying buffers with `aclrtFree`.

The descriptor and the device buffer have independent lifetimes; destroying the `aclTensor` does **not** free the buffer it points to.

## Compact Call Snippet — `aclnnAdd`

The following shows the canonical two-phase flow for the built-in element-wise add. Runtime initialization (`aclInit`, device/context/stream setup) is omitted here — see lang-ascendcl-host-guide.

```cpp
#include "aclnnop/aclnn_add.h"
#include "acl/acl.h"

// Assume xDev, yDev, outDev are device buffers from aclrtMalloc,
// shape {8} of fp16, and 'stream' is a valid aclrtStream.
int64_t shape[] = {8};
int64_t strides[] = {1};

aclTensor* x   = aclCreateTensor(shape, 1, ACL_FLOAT16, strides, 0,
                                 ACL_FORMAT_ND, shape, 1, xDev);
aclTensor* y   = aclCreateTensor(shape, 1, ACL_FLOAT16, strides, 0,
                                 ACL_FORMAT_ND, shape, 1, yDev);
aclTensor* out = aclCreateTensor(shape, 1, ACL_FLOAT16, strides, 0,
                                 ACL_FORMAT_ND, shape, 1, outDev);

aclScalar* alpha = aclCreateScalar(&(float){1.0f}, ACL_FLOAT);

// Phase 1: size the workspace and build the executor.
uint64_t workspaceSize = 0;
aclOpExecutor* executor = nullptr;
aclnnAddGetWorkspaceSize(x, y, alpha, out, &workspaceSize, &executor);

void* workspace = nullptr;
if (workspaceSize > 0) {
    aclrtMalloc(&workspace, workspaceSize, ACL_MEM_MALLOC_HUGE_FIRST);
}

// Phase 2: execute asynchronously on the stream.
aclnnAdd(workspace, workspaceSize, executor, stream);
aclrtSynchronizeStream(stream);

// Cleanup.
if (workspace) aclrtFree(workspace);
aclDestroyScalar(alpha);
aclDestroyTensor(x);
aclDestroyTensor(y);
aclDestroyTensor(out);
```

The end-to-end runnable version of this flow, including device buffer setup and result copy-back, is captured in kernel-vector-add-aclnn.

## From AscendC Kernel to `aclnnXxx` Symbol

A custom operator authored in AscendC becomes an `aclnnYourOp` symbol through the operator-project toolchain, not by manual binding. The standard layout and build path is:

### Project Structure

- **`op_host/`** — host-side definition: the tiling function and the operator prototype (shape/dtype inference, attribute registration). This is plain host C++.
- **`op_kernel/`** — the device kernel written in AscendC (the `Init()`/`Process()` class described in lang-ascendc-guide).

### Build and Install Pipeline

1. **Scaffold** the project with **`msopgen`**, which generates the `op_host` / `op_kernel` skeleton from an operator definition (JSON).
2. **Build** the project; the toolchain compiles the AscendC kernel, links the host tiling/proto, and packages everything into a **custom operator package** installer named like **`custom_opp_<os>_<arch>.run`**.
3. **Install** the run package. It registers the operator into the operator package directory so the runtime can discover it.
4. **Call** it from host code: the package now exports `aclnnYourOpGetWorkspaceSize(...)` and `aclnnYourOp(...)` with the *same* two-phase signature shape as built-in ops. Include the generated `aclnnop/aclnn_your_op.h` and link against the installed op package.

After installation, your custom operator is indistinguishable at the call site from `aclnnAdd` — the only differences are the symbol name and the operator-specific input/output/attribute arguments to `GetWorkspaceSize`.

## Trade-offs, Pitfalls, and Notes

- **Phase ordering is mandatory.** Calling `aclnnXxx` without first calling `aclnnXxxGetWorkspaceSize` (and using the executor it returned) is undefined. The executor is bound to that specific sizing call.
- **Workspace can be zero.** Many ops report `workspaceSize == 0`; guard the `aclrtMalloc` so you do not allocate a zero-byte buffer, and pass `nullptr`/`0` to the execute call in that case.
- **Descriptor vs. buffer lifetime.** `aclDestroyTensor` only frees the descriptor. Forgetting the matching `aclrtFree` on the device buffer leaks device memory.
- **Format matters.** Passing `ACL_FORMAT_ND` when the operator expects `ACL_FORMAT_NZ` (or vice versa) can produce wrong results or an internal layout conversion; match the operator's documented format.
- **Asynchronous execution.** `aclnnXxx` only enqueues work on the stream. Results are not valid until `aclrtSynchronizeStream` returns.
- **aclnn is a caller, not a kernel writer.** If no built-in or installed operator does what you need, you cannot express it purely in aclnn — you must author an AscendC kernel (lang-ascendc-guide) and install it as above before aclnn can reach it.
- **Custom op discovery.** If `aclnnYourOp` is undefined at link/run time, verify the `custom_opp_*.run` package was actually installed and that its operator package directory is on the runtime search path (see lang-ascendcl-host-guide for environment setup).

## Where This Fits

Use aclnn when you want to drive one operator at a time from host C++ — whether a CANN built-in like `aclnnAdd` or a custom AscendC operator you built with `msopgen`. For the device-side authoring of those custom operators, see lang-ascendc-guide; for the surrounding runtime (device, context, stream, memory) that every aclnn call depends on, see lang-ascendcl-host-guide; and for a complete worked example of the full `aclnnAdd` flow, see kernel-vector-add-aclnn.
