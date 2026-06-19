---
id: technique-deepseek-v4-ascend950-runtime
title: "DeepSeek-V4 on Ascend 950 — Compressed Attention Runtime Adaptation"
type: wiki-technique
architectures: [ascend910b]
tags: [deepseek-v4, ascend950, compressed-attention, mxfp, dsa, kv-cache, graph-capture]
confidence: inferred
techniques: [kv-cache-paging, workspace-management, tiling-strategy]
hardware_features: [global-memory, mte]
kernel_types: [attention, moe, gemm]
related: [kernel-flash-attention-npu, kernel-moe-ascendc, kernel-quant-matmul-ascendc, technique-kv-cache-paging, technique-vllm-hybrid-mamba-kv-cache]
sources:
  - "pr-vllm-ascend-9757"
  - "pr-vllm-ascend-9935"
  - "pr-vllm-ascend-10041"
  - "pr-vllm-ascend-10298"
  - "pr-vllm-ascend-10333"
  - "pr-vllm-ascend-10369"
reproducibility: concept
---

# DeepSeek-V4 on Ascend 950 — Compressed Attention Runtime Adaptation

DeepSeek-V4 support on Ascend 950 is not a single kernel patch. It is a runtime adaptation loop spanning quantization, DSA compressed attention, MoE execution, graph capture boundaries, KV-cache semantics, and long-context workspace sizing.

The reusable lesson is: compressed-attention LLMs need a **model-version-aware runtime specialization**. Hardware-specific behavior should be routed through device operators, KV-cache coordinators, and graph-capture policy, not scattered as ad-hoc environment flags at call sites.

## Adaptation Spine

| Area | Main Evidence | Runtime Question |
| --- | --- | --- |
| Base model/hardware support | `pr-vllm-ascend-9757` | How do W4A8 MXFP, DSA, MoE, and model runner paths become reachable? |
| Graph capture boundary | `pr-vllm-ascend-9935` | Which custom attention ops must stay outside piecewise graph capture? |
| Long-context QLI workspace | `pr-vllm-ascend-10041` | Does host tiling allocate workspace matching the Ascend 950 execution path? |
| Compressed prefix cache | `pr-vllm-ascend-10298` | Are cache write and lookup using the same logical block granularity? |
| Runtime default routing | `pr-vllm-ascend-10333` | Can model version replace manual env-gated patch behavior? |
| Graph profiling lifecycle | `pr-vllm-ascend-10369` | Is graph memory profiling running before required KV state exists? |

## Base Support: Quantization, DSA, and MoE

PR #9757 is the trunk. It adds DeepSeek-V4 support for Ascend A5 / Ascend 950 and touches:

- `vllm_ascend/quantization/fp8_config.py`
- `vllm_ascend/quantization/methods/fp8.py`
- `vllm_ascend/quantization/methods/w4a8_mxfp4.py`
- `vllm_ascend/device/device_op.py`
- `vllm_ascend/attention/dsa_v1.py`
- `vllm_ascend/ops/fused_moe/*`
- `vllm_ascend/worker/model_runner_v1.py`

The key shape is a vertical integration: quantization config selects W4A8/MXFP behavior; device ops expose hardware-specific quantized matmul and grouped-matmul/SwiGLU behavior; DSA attention is adapted for A5 metadata and KV interfaces; the model runner makes these paths active during serving.

## Graph Capture Boundary

PR #9935 handles `vllm::dsa_forward` as an attention-like custom op that must be listed in `splitting_ops` for piecewise graph handling. The important nuance is that this is not evidence that every DSA path is freely graph-capturable. It is evidence that DeepSeek-V4 DSA has a graph boundary: keep the custom attention op outside captured subgraphs where needed.

PR #10369 adds another graph lifecycle constraint. Pre-KV ACL graph memory profiling can run before the normal KV-cache-backed graph path exists. For DeepSeek-V4 compressed attention, that temporary path can hit `aclnnScatterNdUpdateV2` errors. The fix skips only pre-KV graph memory profiling for DeepSeek-V4 compressed attention while preserving normal graph capture and replay after KV allocation.

## Long-Context QLI Workspace

PR #10041 fixes `QuantLightningIndexer` workspace sizing for DeepSeek-V4-Flash long-context serving on Ascend 950. The reported failure is an MTE DDR address out-of-range error when sequence length exceeds 300K on 950PR.

The core mechanism is architecture-aware host tiling:

- Ascend 950 score workspace size is computed from aligned `s2Size`.
- The formula uses `s1Base=4` and `s2Base=128`.
- Non-Ascend-950 platforms keep the existing workspace calculation.
- The arch35 preload kernel applies score workspace offset only on AIV, matching the path that uses that buffer.

This is a strong example of a workspace-management pattern: memory errors in MTE code can originate in host-side tiling formulas, not in the device copy loop itself.

## Compressed KV Cache Semantics

PR #10298 fixes compressed prefix-cache lookup. DeepSeek-V4 compressed attention changes block semantics: cache write and lookup must agree on logical compressed block granularity, described in the PR body as `block_size * compress_ratio`.

The patch updates:

- `CompressAttentionManager.cache_blocks()` to write compressed logical block hashes.
- `CompressAttentionManager.find_longest_cache_hit()` to convert incoming physical-granularity hashes.
- Hybrid coordinator logic for alignment, hit length, EAGLE extra length, and truncation.

This distinguishes **physical KV blocks** from **compressed logical blocks**. Mixing them can produce incorrect prefix-cache hits even when all tensor shapes look valid.

## From Env Flag to Model-Version Routing

PR #10333 removes `VLLM_ASCEND_APPLY_DSV4_PATCH`. DeepSeek-V4 behavior is instead applied automatically when KV cache specs carry `model_version="deepseek_v4"`.

That is the right direction for productization:

- Users should not need to remember a hardware/model patch flag.
- Tests should not silently depend on an env var being present.
- The runtime should route model-specific KV/cache behavior from model metadata.

The pattern is broadly useful: when a model family needs special KV-cache or graph behavior, encode it into runtime metadata and coordinators rather than scattering env-gated branches across call sites.

## Failure Modes

| Symptom | Likely Layer | Evidence |
| --- | --- | --- |
| MTE DDR address out-of-range at long sequence | QLI workspace tiling | `pr-vllm-ascend-10041` |
| DSA custom op captured in unsafe graph segment | graph splitting policy | `pr-vllm-ascend-9935` |
| ACL graph profiling fails before KV allocation | graph memory profiling lifecycle | `pr-vllm-ascend-10369` |
| Prefix cache hit is wrong or truncated | compressed logical block hash mismatch | `pr-vllm-ascend-10298` |
| Users forget DSV4 patch env | runtime routing/productization | `pr-vllm-ascend-10333` |

## Design Rules

1. **Route hardware/model differences through device operators.** Quantized matmul, DSA, and MoE paths should live behind device/runtime abstractions.
2. **Keep graph boundaries explicit.** Custom attention ops need clear capture/splitting policy.
3. **Use logical block semantics for compressed KV.** Physical block ids are not enough once compression changes cache granularity.
4. **Make workspace formulas architecture-aware.** Host tiling must match the device path's actual memory accesses.
5. **Replace patch envs with model metadata.** `model_version`-driven routing is safer than manual opt-in flags.

## Related Evidence

- `pr-vllm-ascend-9757` — base DeepSeek-V4 Ascend 950 support.
- `pr-vllm-ascend-9935` — DSA graph capture boundary.
- `pr-vllm-ascend-10041` — QLI long-context workspace sizing.
- `pr-vllm-ascend-10298` — compressed prefix-cache logical block granularity.
- `pr-vllm-ascend-10333` — model-version routing instead of env flag.
- `pr-vllm-ascend-10369` — pre-KV graph memory profiling lifecycle.
