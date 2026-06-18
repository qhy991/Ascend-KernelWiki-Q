---
id: migration-cuda-runtime-to-acl
title: "CUDA Runtime -> AscendCL — Streams, Events, and Device Memory"
type: wiki-migration
tags: [cuda, ascendcl, acl, migration, runtime]
confidence: source-reported
sources: [doc-ascendcl-runtime, doc-ascend-multi-stream-guide, doc-aclnn-operator-api]
from_concept: "CUDA Runtime API"
to_concept: "AscendCL (ACL) Host Runtime"
difficulty: moderate
related: [migration-cuda-to-ascendc, lang-ascendcl-host-guide, migration-memory-model-mapping]
---

## Overview

This guide maps the CUDA Runtime API (the `cuda*` host-side calls) to AscendCL (ACL), the host runtime that drives Ascend NPUs. The translation is mostly one-to-one for device selection, allocation, copy, stream, and event management, but ACL adds an explicit initialization step (`aclInit`) and an explicit Context layer that CUDA hides behind its implicit per-thread context. Most ports are mechanical renames; the real work is restructuring program setup and being explicit about copy lengths and directions.

## Side-by-Side API Mapping

| CUDA Runtime | AscendCL (ACL) | Notes |
|--------------|----------------|-------|
| *(none)* | `aclInit(configPath)` | Must be called once before any other ACL call; no CUDA analog |
| `cudaSetDevice(0)` | `aclrtSetDevice(0)` | Selects the device; in ACL this also creates a **default Context** bound to the calling thread |
| *(implicit context)* | `aclrtCreateContext(&ctx, deviceId)` | Explicit Context object; often created so you own its lifecycle (CUDA has no public analog) |
| *(implicit)* | `aclrtSetCurrentContext(ctx)` | Bind a Context to the current thread |
| `cudaMalloc(&p, size)` | `aclrtMalloc(&p, size, ACL_MEM_MALLOC_HUGE_FIRST)` | Device memory; a huge-page policy flag is **required**, see below |
| `cudaMemcpy(d, s, n, kind)` | `aclrtMemcpy(d, dLen, s, sLen, kind)` | Synchronous; ACL takes **both** dst and src lengths |
| `cudaMemcpyAsync(d, s, n, kind, stream)` | `aclrtMemcpyAsync(d, dLen, s, sLen, kind, stream)` | Async on a stream; same dual-length signature |
| `cudaMemcpyHostToDevice` | `ACL_MEMCPY_HOST_TO_DEVICE` | Direction enum |
| `cudaMemcpyDeviceToHost` | `ACL_MEMCPY_DEVICE_TO_HOST` | Direction enum |
| `cudaMemcpyDeviceToDevice` | `ACL_MEMCPY_DEVICE_TO_DEVICE` | Direction enum |
| `cudaMemcpyHostToHost` | `ACL_MEMCPY_HOST_TO_HOST` | Direction enum |
| `cudaStreamCreate(&s)` | `aclrtCreateStream(&s)` | Creates an async execution queue |
| `cudaStreamSynchronize(s)` | `aclrtSynchronizeStream(s)` | Blocks host until the stream drains |
| `cudaStreamDestroy(s)` | `aclrtDestroyStream(s)` | Release the stream |
| `cudaEventCreate(&e)` | `aclrtCreateEvent(&e)` | Event handle |
| `cudaEventRecord(e, s)` | `aclrtRecordEvent(e, s)` | Record a marker into a stream |
| `cudaStreamWaitEvent(s, e, 0)` | `aclrtStreamWaitEvent(s, e)` | Make a stream wait on an event (cross-stream dep) |
| `cudaEventSynchronize(e)` | `aclrtSynchronizeEvent(e)` | Block host on an event |
| `cudaEventDestroy(e)` | `aclrtDestroyEvent(e)` | Release the event |
| `cudaFree(p)` | `aclrtFree(p)` | Free device memory from `aclrtMalloc` |
| `cudaFreeHost(p)` / `cudaMallocHost` | `aclrtFreeHost(p)` / `aclrtMallocHost(&p, size)` | Pinned host memory |
| `cudaDeviceReset()` | `aclrtResetDevice(deviceId)` | Tear down device-side resources |
| *(none)* | `aclFinalize()` | Mirrors `aclInit`; called once at the very end |

For the kernel-side and AscendC compute-API equivalents (not host runtime), see migration-cuda-to-ascendc and migration-api-equivalents.

## Program Structure Differences

### Explicit init / finalize

CUDA lazily initializes the runtime on first use. ACL requires an explicit bracket: `aclInit` at startup and `aclFinalize` at shutdown, with everything else nested inside.

### The Context layer

In CUDA, calling `cudaSetDevice` implicitly binds a primary context to the current host thread. In ACL the Context is a first-class object. `aclrtSetDevice` will create a default Context for you, which is enough for single-threaded programs. For multi-threaded host code, create Contexts explicitly with `aclrtCreateContext` and bind them per thread with `aclrtSetCurrentContext`, because a Context is **not** automatically shared across threads. Streams and device allocations belong to the Context that was current when they were created. Multi-stream patterns are covered in lang-ascendcl-host-guide.

## Before / After

**Before (CUDA Runtime):**

```cpp
cudaSetDevice(0);

float *dSrc = nullptr, *dDst = nullptr;
size_t bytes = N * sizeof(float);
cudaMalloc(&dSrc, bytes);
cudaMalloc(&dDst, bytes);

cudaStream_t stream;
cudaStreamCreate(&stream);

cudaMemcpyAsync(dSrc, hSrc, bytes, cudaMemcpyHostToDevice, stream);
// ... launch kernel on stream ...
cudaMemcpyAsync(hDst, dDst, bytes, cudaMemcpyDeviceToHost, stream);

cudaStreamSynchronize(stream);

cudaStreamDestroy(stream);
cudaFree(dSrc);
cudaFree(dDst);
cudaDeviceReset();
```

**After (AscendCL):**

```cpp
aclInit(nullptr);                       // no CUDA analog
aclrtSetDevice(0);                      // also creates a default Context

aclrtContext ctx;                       // optional but explicit
aclrtCreateContext(&ctx, 0);
aclrtSetCurrentContext(ctx);

void *dSrc = nullptr, *dDst = nullptr;
size_t bytes = N * sizeof(float);
aclrtMalloc(&dSrc, bytes, ACL_MEM_MALLOC_HUGE_FIRST);
aclrtMalloc(&dDst, bytes, ACL_MEM_MALLOC_HUGE_FIRST);

aclrtStream stream;
aclrtCreateStream(&stream);

// dual-length signature: dst length AND src length
aclrtMemcpyAsync(dSrc, bytes, hSrc, bytes,
                 ACL_MEMCPY_HOST_TO_DEVICE, stream);
// ... launch operator on stream ...
aclrtMemcpyAsync(hDst, bytes, dDst, bytes,
                 ACL_MEMCPY_DEVICE_TO_HOST, stream);

aclrtSynchronizeStream(stream);

aclrtDestroyStream(stream);
aclrtFree(dSrc);
aclrtFree(dDst);
aclrtDestroyContext(ctx);
aclrtResetDevice(0);
aclFinalize();                          // no CUDA analog
```

## Event-Based Cross-Stream Dependencies

The event pattern carries over directly. Record an event on a producer stream, then have a consumer stream wait on it:

```cpp
aclrtEvent done;
aclrtCreateEvent(&done);

aclrtRecordEvent(done, producerStream);     // mark producer progress
aclrtStreamWaitEvent(consumerStream, done); // consumer waits, no host stall

// ... work on consumerStream now safely sees producer results ...

aclrtSynchronizeEvent(done);                // host-side wait, if needed
aclrtDestroyEvent(done);
```

This is the ACL equivalent of `cudaEventRecord` + `cudaStreamWaitEvent`, and it is the recommended way to express inter-stream ordering without serializing on the host.

## Trade-offs, Pitfalls, and Notes

- **Huge-page malloc policy.** `aclrtMalloc` requires a policy argument with no CUDA counterpart. `ACL_MEM_MALLOC_HUGE_FIRST` tries large pages and falls back to normal pages; `ACL_MEM_MALLOC_HUGE_ONLY` fails if huge pages are unavailable; `ACL_MEM_MALLOC_NORMAL_ONLY` uses normal pages. Use `HUGE_FIRST` as the safe default for large device buffers.
- **128-byte alignment.** Buffers returned by `aclrtMalloc` are aligned for the NPU's memory transfer engine. When you compute offsets into a device buffer by hand, keep sub-allocations at 128-byte boundaries so the MTE path stays on its fast alignment; misaligned slices can force slower padded copies.
- **Dual lengths on every copy.** `aclrtMemcpy` / `aclrtMemcpyAsync` take both a destination length and a source length. Passing the wrong destination length is a common porting bug because the CUDA call had only one size argument — the ACL runtime validates the destination capacity, so an under-sized `dstLen` is rejected rather than silently truncating.
- **No implicit context across threads.** A Context made current on one host thread is not visible to another. In multi-threaded hosts, call `aclrtSetCurrentContext` on each worker thread, or you will get "context not set" failures on otherwise-correct copies and launches.
- **Init/finalize bracket.** Forgetting `aclInit` makes the first ACL call fail; forgetting `aclFinalize` can leak driver resources at exit. Treat them like an RAII bracket around the whole program.
- **No unified memory.** ACL has no `cudaMallocManaged` equivalent — host and device buffers are distinct and you must copy explicitly. See migration-memory-model-mapping for the full host/device memory translation.

| Concern | CUDA | AscendCL |
|---------|------|----------|
| Runtime init | Lazy / implicit | Explicit `aclInit` / `aclFinalize` |
| Context | Implicit per-thread primary context | Explicit `aclrtContext`, not shared across threads |
| Malloc policy | Single `cudaMalloc(ptr, size)` | Policy flag required (`ACL_MEM_MALLOC_HUGE_FIRST`, ...) |
| Copy signature | One length | Dst length **and** src length |
| Unified memory | `cudaMallocManaged` | Not available; explicit copies |

## Migration Checklist

1. Wrap `main` (or your runtime init/teardown) with `aclInit` / `aclFinalize`.
2. Replace `cudaSetDevice` with `aclrtSetDevice`; add explicit Context management if the host is multi-threaded.
3. Rename allocation, copy, stream, and event calls per the mapping table.
4. Add the huge-page policy flag to every `aclrtMalloc`.
5. Expand every copy call to the dual-length signature and pick the right `ACL_MEMCPY_*` direction enum.
6. Verify alignment assumptions for any hand-computed buffer offsets (128-byte boundaries).

## References

- [lang-ascendcl-host-guide](/Users/haiyan/Documents/Infinity/Agent4Kernel/Ascend-KernelWiki-Q/wiki/languages/ascendcl-host-guide.md) — full AscendCL host API and multi-stream usage
- [migration-cuda-to-ascendc](/Users/haiyan/Documents/Infinity/Agent4Kernel/Ascend-KernelWiki-Q/wiki/migration/cuda-to-ascendc.md) — kernel-side (device) porting
- [migration-memory-model-mapping](/Users/haiyan/Documents/Infinity/Agent4Kernel/Ascend-KernelWiki-Q/wiki/migration/memory-model-mapping.md) — host/device memory translation
