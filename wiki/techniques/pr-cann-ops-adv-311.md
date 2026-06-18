---
id: technique-pr-cann-ops-adv-311
title: "PR Insight: Ascend/cann-ops-adv #311"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - elementwise
  - data-reuse
  - auto-tuning
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/311"
---

# PR Insight: Ascend/cann-ops-adv #311

**Title:** MoeTokenUnpermuteGrad auto-sync=on

## Overview
This PR enables automatic synchronization (auto-sync=on) for the MoeTokenUnpermuteGrad operator. The change likely improves performance or correctness by automatically managing synchronization points in the MoE token unpermutation gradient computation.

## Technical Significance
Automatic synchronization in gradient operators can improve performance by reducing unnecessary synchronization overhead while ensuring correctness. The MoE token unpermutation operation reverses token ordering from expert assignment during backpropagation. Enabling auto-sync likely optimizes the interaction between Ascend's instruction queue, event sync mechanisms, and memory operations, reducing pipeline bubbles and improving throughput for MoE model training.

## Related
- `technique-moe-ascendc`
- `technique-event-sync`
- `technique-pipeline-scheduling`
- `technique-auto-tuning`