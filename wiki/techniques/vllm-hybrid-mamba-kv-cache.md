---
id: technique-vllm-hybrid-mamba-kv-cache
title: "vLLM Ascend Hybrid/Mamba KV Cache — Group-Aware Transfer and Prefix Caching"
type: wiki-technique
architectures: [ascend910, ascend910b]
tags: [vllm, hybrid-model, mamba, kv-cache, prefix-cache, mooncake, ascend-store]
confidence: inferred
techniques: [kv-cache-paging, workspace-management]
hardware_features: [global-memory]
kernel_types: [attention, paged-attention]
related: [technique-kv-cache-paging, kernel-paged-attention-npu, kernel-flash-attention-npu, technique-deepseek-v4-ascend950-runtime]
sources:
  - "pr-vllm-ascend-9533"
  - "pr-vllm-ascend-10009"
  - "pr-vllm-ascend-10077"
  - "pr-vllm-ascend-10202"
  - "pr-vllm-ascend-10217"
  - "pr-vllm-ascend-10255"
  - "pr-vllm-ascend-10342"
reproducibility: concept
---

# vLLM Ascend Hybrid/Mamba KV Cache — Group-Aware Transfer and Prefix Caching

Hybrid and Mamba-family models make KV cache management more complex than a single attention KV tensor. The runtime may need to coordinate attention KV, compressed KV, sliding-window KV, and Mamba/state groups. In vllm-ascend, this affects AscendStore, Mooncake, prefix caching, PD disaggregation, and layerwise KV pooling.

## Core Problem

Many KV-transfer bugs reduce to one incorrect assumption:

> A single `block_id * block_len` interpretation is enough for all cache groups.

That assumption fails for hybrid/Mamba models. Each cache group can have its own shape, block length, hash granularity, layer mapping, and transfer eligibility. The runtime must be group-aware.

## Evidence Matrix

| PR | Role | Key Mechanism |
| --- | --- | --- |
| #9533 | AscendStore hybrid/Mamba prefix cache | Align prefix cache for hybrid/Mamba cache groups. |
| #10009 | D-side partial-group caching | Skip or account for Mamba groups correctly in PD remote-prefill hit logic. |
| #10342 | Mooncake DeepSeek-V4/hybrid support | Mixed KV group layouts and offsets in Mooncake connector paths. |
| #10202 | PP/MTP layer index correctness | Avoid global/per-stage layer index collision in Mooncake connector. |
| #10217 | Grouped hash lookup encoding | Align grouped hash lookup/store rehash input encoding. |
| #10077 | Layerwise KV Pooling | Reduce metadata/transfer stalls through layerwise save/load scheduling. |
| #10255 | SWA transfer trim ordering | Avoid stale SWA tail blocks reaching sparse attention. |

Only some of these are currently materialized as source pages in this repository. The technique still matters because the bug pattern repeats across connectors.

## AscendStore Route

AscendStore PRs such as #9533 and #10217 focus on key/hash semantics. Prefix-cache hit lookup must encode cache groups consistently. If store and lookup use different encodings, a group can miss cache unnecessarily or hit the wrong block range.

The design rule is simple: cache keys should be derived from the cache group's logical semantics, not from a flat physical block assumption.

## Mooncake Route

Mooncake PRs such as #10342 and #10202 focus on layout and layer mapping. For hybrid models, different groups can have different offsets and shapes. Under pipeline parallelism, layer indices can be global while a stage-local connector only owns a subset of layers. MTP virtual layers add another source of collision.

The design rule is: connector metadata must distinguish global layer id, stage-local layer id, virtual layer id, and cache-group id.

## Layerwise KV Pooling

`pr-vllm-ascend-10077` adds layerwise KV Pooling. Instead of treating KV movement as one bulk operation, layerwise transfer saves or loads KV per layer and overlaps transfer with adjacent layer compute.

For hybrid/Mamba models, layerwise transfer makes metadata discipline more important. The runtime must know which layer and which cache group is being saved or loaded; otherwise a performance optimization can become a correctness bug.

## SWA Stale Block Pattern

`pr-vllm-ascend-10255` is a concrete micro-case: SWA transfer block IDs must be trimmed by actual prompt length before window clipping. If stale tail blocks are sent to `npu_sparse_attn_sharedkv`, attention can produce NaNs and the request can get stuck.

The broader lesson is that block lists are data, not just metadata. A stale block id can point to allocated but unwritten cache.

## Design Rules

1. Treat cache group id as a first-class dimension.
2. Keep physical block ids separate from logical compressed or SWA block semantics.
3. Make prefix-cache hash granularity match write granularity.
4. Keep global, stage-local, and virtual layer ids distinct.
5. Trim invalid transfer blocks before applying group-specific clipping/windowing.
6. Add tests with hybrid groups, Mamba groups, PP, MTP, SWA, and PD disaggregation together.
