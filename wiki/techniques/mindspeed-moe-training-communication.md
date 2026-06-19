---
id: technique-mindspeed-moe-training-communication
title: "MindSpeed MoE Training Communication — P2P, All-to-All Overlap, and Token Permute Fusion"
type: wiki-technique
architectures: [ascend910, ascend910b]
tags: [mindspeed, moe, communication, pipeline-parallel, alltoall-overlap, token-dispatch]
confidence: inferred
techniques: [hccl-optimization]
hardware_features: [hccs, global-memory]
kernel_types: [moe]
related: [technique-hccl-optimization, kernel-moe-ascendc, technique-sgl-deepep-moe-communication, technique-mla-ring-context-parallel]
sources:
  - "pr-mindspeed-2707"
  - "pr-mindspeed-2730"
  - "pr-mindspeed-2703"
reproducibility: concept
---

# MindSpeed MoE Training Communication — P2P, All-to-All Overlap, and Token Permute Fusion

MindSpeed's high-value Ascend training PRs show three related communication optimizations: pipeline-parallel P2P selection, MoE all-to-all compute/communication overlap, and fused token permute/unpermute for MoE routing.

These are not AICore math kernels, but they are just as important for end-to-end throughput. MoE training often bottlenecks on communication and token reordering around expert computation.

## Main Threads

| Thread | Evidence | Optimization Target |
| --- | --- | --- |
| Pipeline P2P | `pr-mindspeed-2707` | Replace batch P2P with explicit `isend` / `irecv` on NPU PP paths. |
| MoE all-to-all overlap | `pr-mindspeed-2730` | Reorder token dispatch, GroupedMLP, and async all-to-all in MindSpore MoE. |
| Fused token permute | `pr-mindspeed-2703` | Use `torch_npu` fused token permute/unpermute with routing maps. |

## Pipeline P2P: Avoiding the Wrong Collective Shape

PR #2707 adds `optimize_p2p_comm` for pipeline parallelism. Its mechanism is simple but important: set `config.batch_p2p_comm = False` and use point-to-point `isend` / `irecv` behavior instead of a batched P2P primitive.

The lesson is that a “more batched” communication API is not automatically faster on every backend. NPU pipeline stages can benefit from explicit P2P scheduling when batch P2P adds overhead or mismatches the pipeline schedule.

## MoE All-to-All Overlap

PR #2730 changes the MindSpore MoE overlap path in:

- `grouped_mlp_with_comp_and_comm_overlap_all2all.py`
- `legacy_a2a_token_dispatcher.py`
- `moe_layer_overlap_all2all.py`

The goal is to hide expert-parallel all-to-all communication behind GroupedMLP compute. This is a control-flow and autograd-ordering optimization: the implementation must preserve saved tensors and backward communication order while moving communication earlier or later to overlap with compute.

## Fused Token Permute

PR #2703 adds a fused MoE permutation feature that calls `torch_npu` fused routing-map operators such as `npu_moe_token_unpermute_with_routing_map`.

MoE dispatch does more than communicate. It also reorders tokens into expert-major layout and restores the original order after expert computation. If token permute/unpermute runs through generic Python or unfused tensor operations, the memory movement and dispatch overhead can become visible. Fusing this step keeps routing-map semantics close to the NPU operator.

## Relationship to ModelLink

ModelLink PRs such as the DeepSeek/Qwen MoE scripts are useful as deployment evidence, but they are not the primary mechanism sources for this technique. They show how users enable the lower-level capabilities through training flags, for example all-to-all overlap, HCCL all-to-all algorithm settings, expert parallelism, and MoE dispatcher choices.

For core mechanism evidence, prefer the MindSpeed PRs that modify communication and fusion code directly.

## Failure Modes

- **Rank mismatch:** P2P and all-to-all choices must be consistent across pipeline or expert-parallel ranks.
- **Autograd ordering bugs:** overlap paths must save the right tensors and replay communication in a valid backward order.
- **Routing-map mismatch:** fused permute/unpermute must use the same routing-map semantics as token dispatch.
- **Backend overgeneralization:** an optimization for NPU P2P may not apply to another backend's batch P2P implementation.

## Design Rules

1. Treat communication API choice as a backend-specific performance decision.
2. Separate token routing/reordering cost from expert GEMM cost when profiling MoE.
3. Validate overlap paths in both forward and backward.
4. Prefer source PRs that modify communication/fusion code over script-only PRs when documenting mechanisms.
