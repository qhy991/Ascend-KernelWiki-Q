---
id: technique-training-communication-scheduling-overlap
title: "Training Communication Scheduling for MoE and Param-Gather Overlap"
type: wiki-technique
architectures: [ascend910, ascend910b]
tags: [mindspeed, moe, alltoall, param-gather, overlap, communication, scheduling]
confidence: source-reported
sources: [pr-mindspeed-2828, pr-mindspeed-2823, pr-mindspeed-2730, pr-mindspeed-2707]
techniques: [hccl-optimization, tensor-parallel-overlap]
hardware_features: [hccs, global-memory]
kernel_types: [moe, grouped-gemm, matmul]
related: [technique-mindspeed-moe-training-communication, technique-tensor-parallel-overlap]
---

# Training Communication Scheduling for MoE and Param-Gather Overlap

MindSpeed PR evidence shows two complementary training-communication ideas: communicate exactly the token counts MoE needs, and launch distributed parameter communication in the order where it can overlap useful compute.

## Variable-Count MoE All-to-All

MoE dispatch naturally produces uneven token counts per expert and rank. A variable-count all-to-all path lets the dispatcher pass true per-rank counts to the communication primitive. This reduces padding pressure and makes the collective contract match the token permutation contract.

Evidence: `pr-mindspeed-2828` proposes `all_to_all_v_c` integration in MindSpore MoE/tensor-parallel paths.

## Bucket-Order Scheduling

Parameter-gather overlap depends on ordering. If a bucket is gathered only when the next computation already needs it, overlap is lost. Recording first-iteration bucket-group trigger order and reusing that order later can turn a reactive gather into a prefetch.

Evidence: `pr-mindspeed-2823` proposes bucket-group order recording and replay around distributed data parallel parameter gather.

## Design Rules

1. **Expose real counts.** MoE dispatch should pass per-rank token counts instead of hiding padding in the collective wrapper.
2. **Keep permutation and collective metadata aligned.** The same expert/rank order must drive token reorder, all-to-all counts, and unpermute.
3. **Observe before replaying order.** Bucket scheduling should be derived from actual trigger order, not guessed statically.
4. **Guard dynamic cases.** Pipeline schedule, recompute, and microbatch changes can invalidate first-iteration bucket order.
5. **Measure TTFT/step time with overlap enabled.** The feature improves latency only if communication lands under compute.

## Relation to Existing MoE Pages

`technique-mindspeed-moe-training-communication` covers MoE all-to-all overlap, P2P optimization, and token permute fusion. This page adds a scheduling layer: variable-count collectives and bucket-order replay are not new kernels, but they change when and how distributed work blocks those kernels.
