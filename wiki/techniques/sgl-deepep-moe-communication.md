---
id: technique-sgl-deepep-moe-communication
title: "SGL DeepEP MoE Communication — Strategy, All-to-All, CCU, and MXFP8"
type: wiki-technique
architectures: [ascend910, ascend910b]
tags: [sglang, deepep, moe, alltoall, ccu, mxfp8, communication]
confidence: inferred
techniques: [hccl-optimization, tiling-strategy]
hardware_features: [hccs, global-memory]
kernel_types: [moe]
related: [technique-hccl-optimization, kernel-moe-ascendc, pattern-host-dispatch-bound]
sources:
  - "pr-sgl-kernel-npu-004"
  - "pr-sgl-kernel-npu-478"
reproducibility: concept
---

# SGL DeepEP MoE Communication — Strategy, All-to-All, CCU, and MXFP8

SGL's DeepEP path on Ascend is best read as a communication-control-plane evolution, not as isolated PRs. The relevant PR chain separates **how callers ask for MoE dispatch/combine** from **which backend actually moves tokens between expert-parallel ranks**.

## Problem Background

An MoE layer has two communication-heavy phases:

1. **Dispatch:** route token activations to the ranks that own selected experts.
2. **Combine:** return expert outputs to the original token order and apply expert weights.

For prefill or large batches, the problem is bandwidth-heavy. For decode, token counts are small and latency dominates. DeepEP therefore needs both normal and low-latency paths, plus a way to select communication backends without changing model code.

## Control Plane Evolution

| Step | PR | Role |
| --- | --- | --- |
| Normal all-to-all mode | #508 | Introduced `DEEP_USE_ALLTOALL_MODE=1` and a Python all-to-all path for normal DeepEP mode. |
| Strategy abstraction | #540 | Moved `Buffer` behavior behind `ep_strategy.py`, `normal_strategy.py`, and `low_latency_strategy.py`. |
| Low-latency all-to-all | #546 | Encapsulated all-to-all inside low-latency strategy while preserving `low_latency_dispatch` / `low_latency_combine`. |
| CCU offload path | #478 | Added `MOE_ENABLE_CCU` low-latency dispatch/combine path with CCU-specific tiling and kernel headers. |
| MXFP8 normal dispatch | #532 | Added A5 normal dispatch MXFP8 support and shared quantization helpers. |
| MXFP8 low-latency dispatch | #549 | Extended MXFP8 into low-latency dispatch with `use_ue8m0` / `quant_mode=3`. |

The important architectural move is #540: once DeepEP communication is represented as a strategy, later features can add all-to-all, CCU, and MXFP8 branches without forcing callers to learn a new public API for each backend.

## Data Plane Branches

DeepEP's data plane has several layers:

- **Python strategy layer:** chooses normal vs low-latency behavior and maps user-facing APIs to backend operations.
- **CANN op layer:** wraps fused MoE dispatch/combine ops such as `npu_moe_distribute_dispatch_v2` and `npu_moe_distribute_combine_v2`.
- **CCU path:** uses CCU-specific host tiling and kernel headers when `MOE_ENABLE_CCU` is enabled.
- **Quantized path:** uses distinct quantization modes, including MXFP8 / `use_ue8m0`, for routed activations.

This split matters because “all-to-all support” can refer to different layers. A Python all-to-all strategy is not the same as a CCU kernel path, and neither is the same as enabling MXFP8 quantization in the routed activation payload.

## CCU Path

PR #478 adds CCU-specific dispatch and combine paths:

- `moe_distribute_dispatch_v2_ccu_tiling.cpp`
- `moe_distribute_combine_v2_ccu_tiling.cpp`
- `moe_distribute_dispatch_v2_ccu.h`
- `moe_distribute_combine_v2_ccu.h`
- shared `quantize_functions.h`

The PR body is explicit about the limitation: the CCU interface is still encapsulated by HCCL, so outer-layer calls require data movement and distribution results are available only after the HCCL-side operator completes communication. That makes #478 a functional offload path and a useful design milestone, but not proof that CCU performance has reached its final form.

Two operational caveats follow:

- `MOE_ENABLE_CCU` must be set consistently across ranks.
- Deferred cases such as `topk=-1` and `bs=0` should not be assumed supported in CCU mode.

## Low-Latency All-to-All

PR #546 wraps all-to-all internally while keeping the external API stable:

```python
packed_recv_x, packed_recv_count, handle, event, hook = buffer.low_latency_dispatch(...)
combined_x, event, hook = buffer.low_latency_combine(...)
```

That API shape is important. Model code should express “dispatch” and “combine,” while the strategy layer decides whether the backend uses a default runtime path, an ops path, all-to-all, CCU, or a future variant.

This is also why #546 should be linked to the older source page `pr-sgl-kernel-npu-004`: that page already documents the PR as upstream evidence and describes the CANN fused dispatch/combine ops behind the Python API.

## MXFP8 Dispatch Path

PR #532 adds MXFP8 support to normal dispatch. PR #549 moves the same idea into low-latency dispatch. The key distinction is mode-specific routing:

- Normal dispatch adds A5/C310-oriented host tiling, kernel branches, and shared quantization helpers.
- Low-latency dispatch exposes `use_ue8m0` and routes it to a separate quantization mode, commonly described in the PR chain as `quant_mode=3`.

This is not just dtype plumbing. MoE dispatch sends token activations across ranks; quantizing routed activations changes communication volume and scale semantics. A wrong scale convention can be a silent correctness bug even if tensor shapes line up.

## Failure Modes and Checks

- **Rank divergence:** every rank must select the same communication strategy and quantization mode.
- **Dispatch/combine mismatch:** upgrading dispatch without matching combine semantics breaks token reconstruction.
- **Environment drift:** `DEEP_USE_ALLTOALL_MODE` and `MOE_ENABLE_CCU` are control-plane inputs; inconsistent deployment can hang collectives.
- **Unsupported CCU cases:** `topk=-1` and `bs=0` were explicitly deferred in the CCU PR body.
- **Scale mismatch:** MXFP8/UE8M0 scale layout must match the kernel path and receiving operator.

## Evidence Index

- **#478 / `pr-sgl-kernel-npu-478`:** CCU offload for low-latency dispatch/combine; host tiling, kernel headers, op API wrappers, quant helpers.
- **#508:** initial normal all-to-all mode with Python all-to-all path.
- **#540:** strategy abstraction that moves communication selection out of `Buffer` internals.
- **#546 / `pr-sgl-kernel-npu-004`:** low-latency all-to-all encapsulation behind `low_latency_dispatch` / `low_latency_combine`.
- **#532:** A5 normal dispatch MXFP8 and quant helper extraction.
- **#549:** low-latency dispatch MXFP8 / `use_ue8m0` extension.

## When to Use This Page

Use this page when deciding where to place a DeepEP change:

- Public API behavior belongs in the strategy layer.
- Host tiling and kernel branch behavior belongs in dispatch/combine operator pages.
- Communication algorithm choices belong with HCCL/CCU discussion.
- Quantization payload changes belong with MXFP8/scale semantics.
