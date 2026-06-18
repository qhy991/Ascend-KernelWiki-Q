---
id: technique-pr-vllm-ascend-9104
title: "PR Insight: vllm-project/vllm-ascend #9104"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - aclgraph
  - causal-conv1d
  - rgdr
  - performance
  - qwen3.5
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9104"
---

# PR Insight: vllm-project/vllm-ascend #9104

**Title:** [Performance][ops][310p] Support Qwen3.5-Dense ACLGraph with fused operators

## Overview
This PR enables ACLGraph graph mode support for Qwen3.5-Dense models on Ascend 310P by updating the causal-conv1d operator and integrating the RGDR (Recurrent Gated Delta Rule) operator. The changes modify the causal_conv1d_v310 tiling implementation and torch binding to support graph capture.

## Technical Significance
ACLGraph graph mode enables better performance optimization through kernel fusion and execution graph compilation. By adapting the causal-conv1d operator and integrating RGDR, this PR enables efficient inference of Qwen3.5-Dense models on Ascend 310P hardware, leveraging graph-mode optimizations for improved throughput and reduced latency.

## Related
- `kernel-causal-conv1d-ascendc`, `kernel-rgdr-ascendc`, `technique-operator-fusion`, `kernel-attention-ascendc`