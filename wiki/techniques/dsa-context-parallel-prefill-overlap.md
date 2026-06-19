---
id: technique-dsa-context-parallel-prefill-overlap
title: "DSA Context-Parallel Prefill Overlap on Ascend"
type: wiki-technique
architectures: [ascend910, ascend910b]
tags: [vllm, dsa, context-parallel, prefill, tensor-parallel, allgather, communication]
confidence: source-reported
sources: [pr-vllm-ascend-10169, pr-vllm-ascend-10694]
techniques: [tensor-parallel-overlap, hccl-optimization, kv-cache-paging]
hardware_features: [hccs, global-memory, cube-unit]
kernel_types: [attention, matmul]
related: [technique-tensor-parallel-overlap, technique-kv-cache-paging]
---

# DSA Context-Parallel Prefill Overlap on Ascend

DeepSeek-style attention under context parallelism is a runtime scheduling problem as much as an attention-kernel problem. The prefill stage needs large KV visibility across sequence partitions, while DSA projection and output work still offers local compute that can hide communication.

## Core Idea

Treat DSA context parallelism as a dependency graph:

```text
hidden states -> local projection work
             \-> KV all-gather for remote sequence partitions
o-proj TP weights -> async all-gather
KV/projection readiness -> DSA attention / output projection
```

The optimizer should launch communication as soon as its inputs are available, then spend the waiting window on local projection, KV cache preparation, or other independent work.

## Evidence Chain

- `pr-vllm-ascend-10169` restructures zigzag context-parallel DSA prefill, including KV all-gather and projection overlap.
- `pr-vllm-ascend-10694` moves o-projection tensor-parallel weight all-gather into an asynchronous path for DSA-CP.

Together they show a consistent direction: avoid placing CP/TP collectives at the exact point of use when earlier scheduling can hide their latency.

## Scheduling Rules

1. **Start collectives at the first legal dependency point.** Do not wait until the consumer line if the input is already stable.
2. **Use local projection as overlap filler.** DSA has compute around attention that can run while KV or weight all-gather progresses.
3. **Keep CP and TP semantics separate.** KV all-gather and o-proj weight all-gather serve different consumers and must not share shape assumptions accidentally.
4. **Make readiness explicit.** Async weight transfer needs completion checks before the output projection consumes gathered weights.
5. **Test precision after reordering.** Overlap changes timing and sometimes accumulation order, even when tensor shapes are unchanged.

## Failure Modes

| Symptom | Likely Cause | Evidence |
| --- | --- | --- |
| Prefill speedup disappears | collective launched too late | `pr-vllm-ascend-10169` |
| DSA-CP waits before o-proj | TP weights not gathered asynchronously | `pr-vllm-ascend-10694` |
| Correct shapes but wrong output | CP slice order or precision drift | `pr-vllm-ascend-10169` |
| Rare startup failure | weight patch runs after DSA-CP path starts | `pr-vllm-ascend-10694` |

## Relation to Kernels

The attention kernel still performs the numerical work, but performance is gated by when it receives KV blocks and projection weights. On Ascend multi-NPU systems, HCCS/HCCL scheduling is therefore part of the effective kernel design.
