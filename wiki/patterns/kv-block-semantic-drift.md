---
id: pattern-kv-block-semantic-drift
title: "KV Block Semantic Drift — Physical, Compressed, SWA, and Hybrid Blocks Mixed"
type: wiki-pattern
architectures: [ascend910, ascend910b]
tags: [vllm, kv-cache, prefix-cache, compressed-kv, swa, mooncake, block-hash, debugging, pattern]
confidence: source-reported
sources: [pr-vllm-ascend-10298, pr-vllm-ascend-10255, pr-vllm-ascend-10342, pr-vllm-ascend-10217, pr-vllm-ascend-10202]
symptoms: ["prefix-cache hit length is wrong", "stale SWA blocks transferred", "all-NaN hidden states", "KV transfer fails under pipeline parallelism", "grouped hash lookup misses stored blocks"]
techniques: [kv-cache-paging]
hardware_features: [global-memory]
kernel_types: [attention, paged-attention]
related: [technique-vllm-hybrid-mamba-kv-cache, technique-kv-cache-paging, kernel-paged-attention-npu]
---

# KV Block Semantic Drift — Physical, Compressed, SWA, and Hybrid Blocks Mixed

## Symptom

KV cache behavior fails in ways that look like attention bugs:

- prefix-cache hit length is wrong or truncated;
- decode receives stale SWA blocks;
- hidden states become all-NaN;
- KV transfer fails under pipeline parallelism;
- grouped hash lookup misses blocks that were stored.

## Root Cause

Different cache groups use different block semantics, but runtime code treats them as one flat physical block space. Common drift points include:

- physical block id vs compressed logical block;
- SWA window clipping vs actual prompt length;
- hybrid/Mamba group byte stride;
- hex-string block hash vs raw hash bytes;
- global layer id vs stage-local layer id vs MTP virtual layer id.

## Semantic Dimensions to Separate

| Dimension | Must Be Explicit Because |
| --- | --- |
| cache group id | attention, compressed, SWA, and Mamba groups differ |
| logical block size | compressed KV may use `block_size * compress_ratio` |
| byte stride | mixed layouts cannot use `block_id * block_len` blindly |
| hash encoding | hex strings and raw bytes hash differently |
| layer index scope | PP and MTP can collide if global/stage/virtual ids are mixed |

## Fix Pattern

- Treat cache group id as a first-class field.
- Convert hash inputs to the same byte representation before rehashing.
- Store byte stride or layout metadata with transfer handshakes.
- Compute prefix-cache hits at the correct logical block granularity.
- Trim invalid transfer blocks by actual prompt length before SWA clipping.
- Use global layer count when assigning virtual layer ids.

## Test Matrix

- hybrid model with Mamba/state group;
- compressed KV prefix-cache hit and miss;
- SWA tail block transfer;
- Mooncake / AscendStore connector variants;
- pipeline parallel with MTP virtual layers;
- grouped hash lookup/store round trip.

## Evidence Matrix

- `pr-vllm-ascend-10298` — compressed prefix-cache logical block granularity.
- `pr-vllm-ascend-10255` — stale SWA transfer blocks from wrong trim/clip order.
- `pr-vllm-ascend-10342` — Mooncake mixed KV layout uses per-block byte stride.
- `pr-vllm-ascend-10217` — grouped hash lookup decodes hex strings to raw bytes.
- `pr-vllm-ascend-10202` — global vs per-stage layer count collision under PP/MTP.
