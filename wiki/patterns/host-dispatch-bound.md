---
id: pattern-host-dispatch-bound
title: "Host-Dispatch-Bound Kernel — Launch Overhead Dominates"
type: wiki-pattern
architectures: [ascend910, ascend910b]
tags: [host-bound, dispatch, diagnosis, performance, pattern]
confidence: inferred
symptoms: ["NPU idle gaps between kernels in msprof timeline", "small per-op device time but high end-to-end latency", "high aclrt host API time", "throughput barely improves with larger batch"]
techniques: [pipeline-scheduling]
related: [lang-ascendcl-host-guide, technique-tiling-strategy, pattern-pipeline-stall]
sources: [doc-ascend-profiling-guide, doc-ascend-multi-stream-guide, doc-ascendcl-runtime]
---

# Host-Dispatch-Bound Kernel Pattern

A host-dispatch-bound workload leaves the NPU idle between tiny kernels because the host CPU — Python framework overhead plus the ACLRT launch path — cannot enqueue operators fast enough to keep the device busy. Unlike [pattern-pipeline-stall](pattern-pipeline-stall), where the stall is *inside* one kernel's queues, here the device finishes each kernel and then waits for the host to deliver the next one. This is *inferred* from common profiling signatures; confirm against your own `msprof` capture before acting.

## Problem

The Ascend execution model is asynchronous: the host thread submits each operator via the runtime, the runtime pushes it onto a stream, and the device executes in order. When individual kernels are very short (microseconds of device time) and there are many of them, the *per-launch host cost* — Python dispatch, shape inference, tiling computation, and the `aclrtLaunchKernel` / runtime enqueue itself — exceeds the kernel's device time. The stream drains faster than the host can refill it, so the AICore idles between ops.

This pattern dominates in three situations:

- **Many small ops**: graphs with hundreds of tiny element-wise / reshape / cast ops (typical of un-fused eager execution).
- **Dynamic shapes**: each new shape triggers recompilation or re-tiling on the host, adding milliseconds of host work before the kernel can even be enqueued.
- **Eager mode**: PyTorch/torch_npu eager dispatch submits one op at a time with full framework overhead per op, with no graph-level batching of launches.

## Diagnostic Symptoms (via msprof)

Collect a timeline with `msprof` and inspect both the device track and the host API track:

- **Idle gaps in the device (AICore) timeline**: visible whitespace between consecutive kernels — the device is waiting, not computing.
- **Small per-op device time, high end-to-end latency**: each kernel reports only a few microseconds, yet wall-clock latency is large.
- **Host API time dominated by launch**: the host-side `aclrtLaunchKernel` (and surrounding runtime/dispatch calls) accounts for a large share of total time, often more than the summed device kernel time.
- **Throughput barely improves with larger batch**: scaling batch size does not raise device utilization, because the bottleneck is the *number* of launches, not the work per launch.

A quick rule of thumb: if `sum(device kernel time) << wall-clock` and the host API track is busy while the device track is idle, you are host-dispatch-bound rather than compute- or memory-bound.

## Root Causes

1. **Op count too high**: many small operators, each paying full per-launch host overhead.
2. **Per-launch host work**: shape inference, tiling selection, and kernel argument packing redone on every call instead of cached.
3. **Single-stream serialization**: all ops enqueued on one stream, so the device cannot work ahead while the host prepares the next op.
4. **Recompilation churn**: dynamic shapes force the host to recompile/retile, stalling the launch pipeline.

## Solutions

Order these by leverage: cutting op count usually wins first, then removing per-launch CPU work, then overlapping host and device.

### 1. Operator Fusion — cut the op count

The most effective fix is to issue fewer, larger kernels. Fusing a chain of element-wise ops (e.g. `add → mul → activation`) into one AscendC kernel collapses many launches into one, eliminating most of the host overhead. See [doc-ascend-operator-fusion](doc-ascend-operator-fusion) for fusion patterns and [technique-tiling-strategy](technique-tiling-strategy) for sizing the fused kernel.

### 2. Graph Mode / npugraph capture — amortize launch over a whole graph

Capture a static sequence of ops once and replay it, so the host pays dispatch cost a single time instead of per iteration. With `torch_npu`, capture with the npugraph API; at the runtime level the same idea is exposed through ACL graph/model execution:

```python
import torch
import torch_npu

device = "npu:0"
model = model.to(device).eval()

# Warm up so shapes/tiling are resolved and kernels are compiled
static_input = torch.randn(batch, dim, device=device)
for _ in range(3):
    _ = model(static_input)
torch.npu.synchronize()

# Capture the op sequence once — host dispatch happens here, not per replay
g = torch_npu.npu.NPUGraph()
with torch_npu.npu.graph(g):
    static_output = model(static_input)

# Replay: device runs the whole captured sequence with ~one launch of host cost
for batch_input in loader:
    static_input.copy_(batch_input)          # update inputs in place
    g.replay()                                # no per-op Python/aclrt dispatch
    torch.npu.synchronize()
    consume(static_output)
```

Capture requires *static* shapes and stable control flow; see the dynamic-shape note below.

### 3. Multi-Stream Overlap — let the device work ahead

Spread independent ops across multiple streams so the device can execute one stream's kernels while the host enqueues onto another. The host launch cost is then hidden behind device execution rather than serialized with it. See [doc-ascend-multi-stream-guide](doc-ascend-multi-stream-guide) and the host-side setup in [lang-ascendcl-host-guide](lang-ascendcl-host-guide).

```c
// ACL host code: two streams overlap host dispatch with device execution
aclrtStream stream0, stream1;
aclrtCreateStream(&stream0);
aclrtCreateStream(&stream1);

for (int i = 0; i < num_tiles; ++i) {
    aclrtStream s = (i % 2 == 0) ? stream0 : stream1;
    // While the device drains the other stream, the host enqueues here
    aclrtLaunchKernel(kernel, blockDim, args[i], argSize, s, /*cfg*/ nullptr);
}

aclrtSynchronizeStream(stream0);
aclrtSynchronizeStream(stream1);
aclrtDestroyStream(stream0);
aclrtDestroyStream(stream1);
```

### 4. Bigger Tiles / Larger Batch — more device work per launch

If op count is fixed, increase the work each launch performs so device time grows relative to host overhead. Larger tiles or batch raise the device-time-to-launch-cost ratio and push the workload out of the host-bound regime (until it becomes compute- or memory-bound instead). Balance against Unified Buffer capacity using [technique-tiling-strategy](technique-tiling-strategy).

### 5. Static-Shape Tiling Cache — stop recomputing tiling

For shapes that repeat, compute and cache the tiling decision so each launch skips host-side re-tiling. This removes the per-call shape-inference/tiling cost that bloats the host API track, and avoids recompilation churn under dynamic shapes by reusing a fixed tiling for known buckets.

## Diagnostic Flowchart

```
Wall-clock latency >> sum(device kernel time)?
├─ Yes → Inspect host API track in msprof
│   ├─ aclrtLaunchKernel dominates host time? → Host-dispatch-bound
│   │   ├─ Many small ops?         → Fuse ops (doc-ascend-operator-fusion)
│   │   ├─ Static op sequence?     → Capture with npugraph / ACL graph
│   │   ├─ Independent ops?        → Multi-stream overlap (doc-ascend-multi-stream-guide)
│   │   ├─ Tiny per-op work?       → Increase tile / batch size
│   │   └─ Dynamic shapes / retile? → Cache tiling for known shape buckets
│   └─ Compilation/retile dominates? → Static-shape tiling cache + shape bucketing
└─ No → Device track is busy → Not host-bound;
        check pattern-pipeline-stall (intra-kernel) or memory/compute bottlenecks
```

## Solution Comparison

| Solution | Attacks | Best when | Cost / constraint |
|----------|---------|-----------|-------------------|
| Operator fusion | Op count | Many small element-wise ops | Requires fused kernel authoring |
| npugraph capture | Per-iteration dispatch | Static shapes, repeated graph | No dynamic shapes/control flow |
| Multi-stream overlap | Serialized launches | Independent ops | Stream/event management complexity |
| Bigger tile / batch | Launch-to-device ratio | Few but tiny kernels | Bounded by UB capacity / memory |
| Static tiling cache | Re-tiling host cost | Recurring or dynamic shapes | Cache invalidation per shape bucket |

## Trade-offs and Pitfalls

- **Fusion is not free**: a fused kernel must fit Unified Buffer and may reduce reuse opportunities; over-fusing can re-introduce intra-kernel stalls — see [pattern-pipeline-stall](pattern-pipeline-stall).
- **Graph capture freezes shapes**: npugraph/ACL graph replay assumes fixed shapes and stable control flow. Dynamic batch sizes break capture and force re-capture; bucket shapes or pad to fixed sizes instead.
- **Multi-stream needs correct synchronization**: overlapping streams without proper events can create data races or hide a *different* bottleneck rather than fix the host one; verify with a fresh `msprof` trace ([doc-ascend-profiling-guide](doc-ascend-profiling-guide)).
- **Bigger batch can flip the bottleneck**: raising batch/tile until the device track fills means the workload may become memory- or compute-bound; re-profile and switch to the corresponding pattern.
- **Confirm before acting**: these signatures are *inferred* from typical host-bound traces. A busy host API track alone is not proof — pair it with visible device idle gaps before committing to a fix.

## Related Pages

- [lang-ascendcl-host-guide](lang-ascendcl-host-guide) — host-side runtime, streams, and the launch path
- [doc-ascend-multi-stream-guide](doc-ascend-multi-stream-guide) — multi-stream overlap setup
- [technique-tiling-strategy](technique-tiling-strategy) — sizing tiles and batches per launch
- [pattern-pipeline-stall](pattern-pipeline-stall) — the intra-kernel counterpart (queue dependency stalls)
