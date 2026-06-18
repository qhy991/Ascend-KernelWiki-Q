---
id: lang-ascendcl-host-guide
title: "AscendCL — Host Runtime Programming (C/C++ and pyACL)"
type: wiki-language
tags: [ascendcl, acl, cpp, python, runtime]
confidence: source-reported
sources: [doc-ascendcl-runtime, doc-aclnn-operator-api, doc-ascend-multi-stream-guide]
architectures: [ascend910, ascend910b, ascend310p]
languages: [cpp, python]
related: [lang-aclnn-cpp-guide, migration-cuda-runtime-to-acl]
---

## Overview

AscendCL (Ascend Computing Language) is the host-side runtime API for Ascend NPUs — the layer responsible for device initialization, memory management, data movement, and asynchronous execution control. It is the functional analogue of the CUDA runtime API: host C/C++ code uses `acl*` functions to acquire a device, allocate device memory, launch operators (via the aclnn library described in [lang-aclnn-cpp-guide](./aclnn-cpp-guide.md)), and synchronize results back to the host. A Python binding, **pyACL**, mirrors the same surface for scripting and prototyping.

## Resource Hierarchy

AscendCL organizes execution around a three-level resource hierarchy. Each level is created on top of the one above it, and teardown happens in reverse order.

- **Device** — a physical NPU, selected by integer ordinal via `aclrtSetDevice(deviceId)`. Binding a device implicitly creates a default Context and a default Stream on the calling thread.
- **Context** — an isolated execution environment that owns streams, events, and a memory address space. Created with `aclrtCreateContext` / destroyed with `aclrtDestroyContext`. A context is bound to exactly one device; one device can host many contexts. Use `aclrtSetCurrentContext` to switch the active context on a thread.
- **Stream** — an ordered queue of tasks (memcpy, operator launches, events). Operations within a stream execute in issue order; operations across streams may overlap. Created with `aclrtCreateStream` / destroyed with `aclrtDestroyStream`.

```
Device (aclrtSetDevice)
  └── Context (aclrtCreateContext)
        └── Stream (aclrtCreateStream)
              └── Tasks: aclrtMemcpyAsync, aclnnXxx, aclrtRecordEvent ...
```

## Initialization and Teardown

The runtime must be initialized exactly once per process before any other ACL call, and finalized exactly once at exit. The canonical sequence is:

| Step | API | Purpose |
|------|-----|---------|
| 1 | `aclInit(configPath)` | Process-wide init; `configPath` may be `nullptr` |
| 2 | `aclrtSetDevice(deviceId)` | Acquire device, create default context + stream |
| 3 | `aclrtCreateContext(&ctx, deviceId)` | (Optional) explicit context for multi-thread/stream |
| 4 | `aclrtCreateStream(&stream)` | (Optional) explicit stream for async overlap |
| ... | *work* | memory, memcpy, operator launches |
| n-3 | `aclrtDestroyStream(stream)` | Release stream |
| n-2 | `aclrtDestroyContext(ctx)` | Release context |
| n-1 | `aclrtResetDevice(deviceId)` | Release device |
| n | `aclFinalize()` | Process-wide teardown |

Every ACL call returns an `aclError`; the success sentinel is `ACL_SUCCESS` (value `0`). Robust host code checks the return of each call rather than assuming success — there is no thrown-exception path.

## Memory Management

AscendCL distinguishes **device memory** (on the NPU HBM) from **host memory** (system RAM), with a separate API for page-locked (pinned) host buffers that enable true asynchronous DMA.

- `aclrtMalloc(&devPtr, size, policy)` — allocate device memory. The recommended `policy` is `ACL_MEM_MALLOC_HUGE_FIRST`, which prefers huge pages and falls back to normal pages when huge pages are unavailable; `ACL_MEM_MALLOC_HUGE_ONLY` and `ACL_MEM_MALLOC_NORMAL_ONLY` exist for explicit control. Allocations are **128-byte aligned**, matching the access granularity the NPU's MTE (Memory Transfer Engine) prefers; sizing buffers to a multiple of 128 bytes avoids partial-line transfers.
- `aclrtFree(devPtr)` — release device memory.
- `aclrtMallocHost(&hostPtr, size)` / `aclrtFreeHost(hostPtr)` — allocate/free page-locked host memory. Pinned host buffers are required for `aclrtMemcpyAsync` to overlap with compute; pageable memory forces a synchronous staging copy.
- `aclrtMemcpy(dst, dstSize, src, srcSize, kind)` — synchronous copy. `kind` is one of `ACL_MEMCPY_HOST_TO_DEVICE`, `ACL_MEMCPY_DEVICE_TO_HOST`, `ACL_MEMCPY_DEVICE_TO_DEVICE`, or `ACL_MEMCPY_HOST_TO_HOST`.
- `aclrtMemcpyAsync(dst, dstSize, src, srcSize, kind, stream)` — asynchronous copy enqueued on a stream; returns immediately. Correctness requires the host buffer to remain valid (and ideally pinned) until the stream reaches the copy.

## Streams and Events for Async Overlap

Asynchronous overlap is the primary host-side performance lever, mirroring the CUDA stream/event model. Tasks issued to *different* streams can execute concurrently — for example, copying the next input tile (H2D on stream B) while an operator runs on the current tile (stream A). Per [doc-ascend-multi-stream-guide](../../sources/docs/ascend-multi-stream-guide.md), well-pipelined multi-stream code overlaps H2D copy, compute, and D2H copy across at least three streams.

Events provide cross-stream ordering and timing:

- `aclrtCreateEvent(&event)` / `aclrtDestroyEvent(event)` — lifecycle.
- `aclrtRecordEvent(event, stream)` — mark a point in a stream.
- `aclrtStreamWaitEvent(stream, event)` — make a stream wait on an event recorded in another stream (dependency without a full host sync).
- `aclrtSynchronizeStream(stream)` — block the host until all tasks on the stream complete.
- `aclrtSynchronizeEvent(event)` — block the host until the event has been recorded.

The general rule: prefer event-based stream dependencies over `aclrtSynchronizeStream` inside the steady-state loop, and reserve host synchronization for the boundaries where results must reach the host.

## Minimal C++ Skeleton

```cpp
#include "acl/acl.h"

int main() {
    // 1. Init runtime, acquire device + explicit context/stream
    aclError ret = aclInit(nullptr);
    if (ret != ACL_SUCCESS) { /* handle */ return -1; }

    int32_t deviceId = 0;
    aclrtSetDevice(deviceId);

    aclrtContext ctx;
    aclrtCreateContext(&ctx, deviceId);

    aclrtStream stream;
    aclrtCreateStream(&stream);

    // 2. Allocate pinned host + device memory (huge-page first)
    size_t size = 4096 * sizeof(uint16_t);   // multiple of 128 bytes
    void *hostBuf = nullptr, *devBuf = nullptr;
    aclrtMallocHost(&hostBuf, size);
    aclrtMalloc(&devBuf, size, ACL_MEM_MALLOC_HUGE_FIRST);

    // 3. Async H2D, launch operator on the same stream, async D2H
    aclrtMemcpyAsync(devBuf, size, hostBuf, size,
                     ACL_MEMCPY_HOST_TO_DEVICE, stream);
    // ... aclnnXxx(...) operator launch on `stream` (see lang-aclnn-cpp-guide) ...
    aclrtMemcpyAsync(hostBuf, size, devBuf, size,
                     ACL_MEMCPY_DEVICE_TO_HOST, stream);

    // 4. Block until the stream drains, then tear down in reverse order
    aclrtSynchronizeStream(stream);

    aclrtFree(devBuf);
    aclrtFreeHost(hostBuf);
    aclrtDestroyStream(stream);
    aclrtDestroyContext(ctx);
    aclrtResetDevice(deviceId);
    aclFinalize();
    return 0;
}
```

## Python Binding — pyACL

pyACL exposes the same runtime under the `acl` module, with submodules grouping the C namespaces (`acl.rt` for the `aclrt*` family). Functions return a value-plus-status tuple, so the trailing `ret` must be checked against `ACL_SUCCESS` exactly as in C++:

```python
import acl

ACL_SUCCESS = 0
ACL_MEM_MALLOC_HUGE_FIRST = 0
ACL_MEMCPY_HOST_TO_DEVICE = 1

ret = acl.init()                         # mirrors aclInit
assert ret == ACL_SUCCESS

acl.rt.set_device(0)                     # mirrors aclrtSetDevice
context, ret = acl.rt.create_context(0)  # mirrors aclrtCreateContext
stream, ret = acl.rt.create_stream()     # mirrors aclrtCreateStream

size = 4096 * 2                          # multiple of 128 bytes
dev_ptr, ret = acl.rt.malloc(size, ACL_MEM_MALLOC_HUGE_FIRST)
# acl.rt.memcpy(dst, dst_size, src, src_size, kind) mirrors aclrtMemcpy
# ... operator launch, then synchronize ...
acl.rt.synchronize_stream(stream)

acl.rt.free(dev_ptr)
acl.rt.destroy_stream(stream)
acl.rt.destroy_context(context)
acl.rt.reset_device(0)
acl.finalize()
```

pyACL is convenient for inference scripting and quick experiments, but it carries Python interpreter overhead on every call and is not suited to the steady-state hot loop of a latency-sensitive serving path — for that, the C++ runtime is preferred.

## Comparison with CUDA Runtime

| Concept | AscendCL | CUDA Runtime |
|---------|----------|--------------|
| Init / teardown | `aclInit` / `aclFinalize` | (implicit) / `cudaDeviceReset` |
| Select device | `aclrtSetDevice` | `cudaSetDevice` |
| Context | `aclrtCreateContext` (explicit) | (implicit primary context) |
| Stream | `aclrtCreateStream` | `cudaStreamCreate` |
| Device alloc | `aclrtMalloc` (huge-first policy) | `cudaMalloc` |
| Pinned host alloc | `aclrtMallocHost` | `cudaMallocHost` |
| Async copy | `aclrtMemcpyAsync` | `cudaMemcpyAsync` |
| Event record/wait | `aclrtRecordEvent` / `aclrtStreamWaitEvent` | `cudaEventRecord` / `cudaStreamWaitEvent` |
| Stream sync | `aclrtSynchronizeStream` | `cudaStreamSynchronize` |
| Success sentinel | `ACL_SUCCESS` | `cudaSuccess` |

See [migration-cuda-runtime-to-acl](../migration/cuda-runtime-to-acl.md) for the full mapping and porting checklist.

## Trade-offs, Pitfalls, and Notes

- **Init/finalize is process-scoped.** Call `aclInit` and `aclFinalize` exactly once. Calling `aclInit` twice, or issuing ACL calls after `aclFinalize`, returns an error.
- **Teardown order matters.** Always release in the reverse of acquisition: stream → context → device → finalize. Destroying a context with live streams or outstanding device memory leaks resources.
- **Context is thread-bound.** A context created on one thread is not automatically current on another; use `aclrtSetCurrentContext` when sharing across threads, or create a context per worker thread.
- **Async needs pinned host memory.** `aclrtMemcpyAsync` against pageable host memory degrades to a synchronous staged copy, silently erasing the overlap you intended. Always pair async copies with `aclrtMallocHost` buffers.
- **Respect 128-byte alignment.** `aclrtMalloc` returns 128-byte-aligned pointers; sizing transfers and tiles to multiples of 128 bytes keeps the MTE on full cache lines and avoids partial-line penalties that surface in the kernels described in [lang-aclnn-cpp-guide](./aclnn-cpp-guide.md).
- **Check every `aclError`.** There is no exception path. A missed error check on `aclrtMalloc` (e.g. out-of-memory) turns into an opaque crash later in `aclrtMemcpy`.
- **Don't over-synchronize.** Replacing event-based dependencies with `aclrtSynchronizeStream` in the inner loop serializes copy and compute and is the most common cause of lost multi-stream overlap (see [doc-ascend-multi-stream-guide](../../sources/docs/ascend-multi-stream-guide.md)).
