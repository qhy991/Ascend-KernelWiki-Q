---
id: doc-ascendcl-runtime
title: "AscendCL (ACL) Host Runtime API Reference"
type: source-doc
architectures: [ascend910, ascend910b, ascend310p]
tags: [ascendcl, acl, cpp, runtime, cann]
date: '2026-02-21'
url: https://www.hiascend.com/document/detail/en/canncommercial/800/inferapplicationdev/aclcppdevg/aclcppdevg_0002.html
hardware_features: [global-memory, hccs]
confidence: verified
---

# AscendCL (ACL) Host Runtime API Reference

AscendCL (ACL) is the C/C++ host-side runtime library in CANN that an application uses to drive Ascend NPUs: it initializes the runtime, manages devices, contexts, and streams, allocates device memory, and moves data between host and device. This page summarizes the host runtime control plane — the calls that surround any kernel launch. For the on-device kernel API, see the AscendC reference (`doc-ascendc-api-reference`); for host-orchestrated overlap of multiple streams, see `doc-ascend-multi-stream-guide`.

## Resource Model

ACL organizes execution around a strict nesting of resources, each of which must be created and later destroyed in reverse order:

```
aclInit                    (process-level runtime init)
  └─ aclrtSetDevice        (bind a device to the thread)
       └─ aclrtCreateContext  (per-device execution context)
            └─ aclrtCreateStream  (ordered task queue)
                 └─ aclrtMalloc / aclrtMemcpyAsync / kernel launches
```

A **context** holds the resources bound to one device for one usage scope. A **stream** is an in-order task queue inside a context; tasks within a stream execute sequentially, while tasks on different streams may run concurrently. Setting a device with `aclrtSetDevice` implicitly creates a default context if none is created explicitly.

## Initialization

```c
// 1. Initialize the ACL runtime once per process.
//    configPath may be NULL or a path to an acl.json config file.
aclError ret = aclInit(configPath);

// 2. Select the device by logical id (0, 1, ...).
ret = aclrtSetDevice(deviceId);

// 3. Create an explicit context bound to the device.
aclrtContext context;
ret = aclrtCreateContext(&context, deviceId);

// 4. Create a stream within the current context.
aclrtStream stream;
ret = aclrtCreateStream(&stream);
```

Every ACL call returns an `aclError`; `ACL_SUCCESS` (value `0`) indicates success. Production code should check each return value, because a failed `aclrtSetDevice` (for example, a device already in use) makes all subsequent calls fail.

## Stream and Event Management

Streams give ordered execution; events give cross-stream synchronization. Recording an event on one stream and waiting on it from another stream lets the host express a dependency without a full device synchronize.

```c
// Stream synchronization: block the host until all tasks on the stream finish.
aclrtSynchronizeStream(stream);

// Event-based cross-stream synchronization.
aclrtEvent event;
aclrtCreateEvent(&event);

// On the producer stream, record the event after the producing tasks.
aclrtRecordEvent(event, producerStream);

// On the consumer stream, wait for the event before dependent tasks run.
// This does NOT block the host; it inserts a wait into the stream's queue.
aclrtStreamWaitEvent(consumerStream, event);

// Optionally query elapsed time or completion state, then clean up.
aclrtDestroyEvent(event);
```

`aclrtSynchronizeStream` is a host-side barrier and serializes the pipeline, so prefer `aclrtRecordEvent` / `aclrtStreamWaitEvent` for ordering work between streams and reserve full synchronization for the points where the host actually needs results back. This event pattern is the foundation of the compute/communication overlap described in `doc-ascend-multi-stream-guide`.

## Device and Host Memory

Device (Global Memory) buffers are allocated with `aclrtMalloc`. The policy argument controls how the allocator treats huge pages:

```c
void *devPtr = NULL;
size_t size = M * N * sizeof(uint16_t);   // fp16 element = 2 bytes (ACL: aclFloat16)

// Prefer huge pages, fall back to normal pages if unavailable.
aclrtMalloc(&devPtr, size, ACL_MEM_MALLOC_HUGE_FIRST);

// ... use devPtr as a kernel argument or memcpy target ...

aclrtFree(devPtr);
```

| Policy                          | Behavior                                                        |
|---------------------------------|----------------------------------------------------------------|
| `ACL_MEM_MALLOC_HUGE_FIRST`     | Try huge pages first; fall back to normal pages on failure     |
| `ACL_MEM_MALLOC_HUGE_ONLY`      | Allocate huge pages only; fail if unavailable                  |
| `ACL_MEM_MALLOC_NORMAL_ONLY`    | Allocate normal pages only                                     |

Huge pages reduce TLB pressure for large, long-lived buffers (weights, activation tensors), so `ACL_MEM_MALLOC_HUGE_FIRST` is the common default. Use `ACL_MEM_MALLOC_NORMAL_ONLY` for many small, short-lived allocations where huge-page fragmentation is not worth it.

Page-locked host memory is allocated with `aclrtMallocHost`. Pinned host buffers are required for fully asynchronous `aclrtMemcpyAsync` transfers, since a pageable host buffer can force the copy to behave synchronously.

```c
void *hostPtr = NULL;
aclrtMallocHost(&hostPtr, size);   // page-locked host buffer
// ... fill hostPtr, use as async-copy source ...
aclrtFreeHost(hostPtr);
```

## Data Transfer

Synchronous and asynchronous copies share the same direction enum. Both take explicit destination and source lengths, which the runtime uses for bounds validation.

```c
// Synchronous host -> device copy (blocks the host until complete).
aclrtMemcpy(devPtr, dstLen, hostPtr, srcLen, ACL_MEMCPY_HOST_TO_DEVICE);

// Asynchronous copy enqueued on a stream (returns immediately).
aclrtMemcpyAsync(devPtr, dstLen, hostPtr, srcLen,
                 ACL_MEMCPY_HOST_TO_DEVICE, stream);

// The async copy is only guaranteed complete after a stream sync.
aclrtSynchronizeStream(stream);
```

| Direction                     | Meaning                          |
|-------------------------------|----------------------------------|
| `ACL_MEMCPY_HOST_TO_DEVICE`   | Host buffer → Global Memory      |
| `ACL_MEMCPY_DEVICE_TO_HOST`   | Global Memory → host buffer      |
| `ACL_MEMCPY_DEVICE_TO_DEVICE` | Global Memory → Global Memory    |

`ACL_MEMCPY_DEVICE_TO_DEVICE` stays on the NPU and, across multiple NPUs, can ride the high-speed HCCS interconnect rather than crossing PCIe, which makes it preferable to a device-to-host-to-device round trip for moving tensors between devices.

### Alignment

Some transfer scenarios require the device address to be **128-byte aligned**. When in doubt, round allocations and offsets up to a 128-byte boundary; `aclrtMalloc` returns suitably aligned base pointers, but manually computed sub-offsets into a larger buffer must preserve alignment to remain valid for those scenarios.

## Teardown

Resources are released in the reverse of the order they were created:

```c
aclrtFree(devPtr);              // free device memory
aclrtDestroyStream(stream);     // destroy streams
aclrtDestroyContext(context);   // destroy explicit contexts
aclrtResetDevice(deviceId);     // release the device
aclFinalize();                  // finalize the ACL runtime
```

`aclrtResetDevice` releases the device's runtime resources and should follow the destruction of all streams and contexts bound to it. `aclFinalize` is the process-level counterpart to `aclInit` and must be the last ACL call.

## End-to-End Skeleton

A minimal host program that uploads inputs, launches a kernel, and reads results back:

```c
aclInit(NULL);
aclrtSetDevice(0);

aclrtContext context;
aclrtCreateContext(&context, 0);
aclrtStream stream;
aclrtCreateStream(&stream);

void *devIn = NULL, *devOut = NULL, *hostIn = NULL;
aclrtMallocHost(&hostIn, size);            // page-locked staging buffer
aclrtMalloc(&devIn,  size, ACL_MEM_MALLOC_HUGE_FIRST);
aclrtMalloc(&devOut, size, ACL_MEM_MALLOC_HUGE_FIRST);

aclrtMemcpyAsync(devIn, size, hostIn, size,
                 ACL_MEMCPY_HOST_TO_DEVICE, stream);
// ... launch kernel on stream (e.g. a matmul, see kernel-matmul-ascendc) ...
aclrtMemcpyAsync(hostIn, size, devOut, size,
                 ACL_MEMCPY_DEVICE_TO_HOST, stream);
aclrtSynchronizeStream(stream);            // host waits for the whole chain

aclrtFree(devIn);
aclrtFree(devOut);
aclrtFreeHost(hostIn);
aclrtDestroyStream(stream);
aclrtDestroyContext(context);
aclrtResetDevice(0);
aclFinalize();
```

## Trade-offs, Pitfalls, and Notes

- **Synchronous vs. asynchronous copy**: `aclrtMemcpy` is simpler but stalls the host on every transfer. `aclrtMemcpyAsync` overlaps copies with compute but only when the host buffer is page-locked (`aclrtMallocHost`) and you explicitly synchronize before reading results.
- **Forgetting the stream sync**: An `aclrtMemcpyAsync` followed by an immediate host read of the destination is a race — the copy may not have finished. Always insert `aclrtSynchronizeStream` (or an event wait) before consuming async results.
- **Alignment**: Some copy scenarios require 128-byte aligned device addresses. Misaligned sub-buffer offsets can fail or silently degrade to a slow path; keep allocations and offsets on 128-byte boundaries.
- **Huge-page policy**: `ACL_MEM_MALLOC_HUGE_ONLY` fails outright if huge pages are exhausted; prefer `ACL_MEM_MALLOC_HUGE_FIRST` unless you specifically need huge pages guaranteed.
- **Teardown order**: Destroying a device (`aclrtResetDevice`) while streams or contexts are still live leaks resources or returns errors. Always tear down in reverse-creation order.
- **Error checking**: Every call returns an `aclError`; a single unchecked `ACL_SUCCESS` violation early in init cascades into confusing downstream failures.
- **Context-per-thread**: A context is bound to the calling scope; multi-threaded hosts should create or set a context per thread rather than sharing one freely.

## Related Pages

- [AscendC API Reference](doc-ascendc-api-reference) — the on-device kernel programming API that ACL launches.
- [Multi-Stream Execution Guide](doc-ascend-multi-stream-guide) — using streams and events for compute/communication overlap.
- [HCCL Collective Communication](doc-hccl-collective) — multi-NPU collectives layered on the same stream/event model.
- [Matmul Kernel](kernel-matmul-ascendc) — a representative kernel driven by this host runtime.

## Status

Verified against CANN 8.0 (AscendCL C/C++ host API). API names and memory/copy enums match the commercial CANN documentation.
