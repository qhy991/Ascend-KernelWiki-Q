---
id: technique-pr-vllm-ascend-9396
title: "PR Insight: vllm-project/vllm-ascend #9396"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek-v4
  - operator-fusion
  - hc-pre
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9396"
---

# PR Insight: vllm-project/vllm-ascend #9396

**Title:** [Feature][Model] Switch DeepSeekV4 hc_pre to fused op

## Overview
This PR switches the DeepSeek V4 hc_pre operation to use a fused custom operator implementation. The change updates the model code, torch bindings, and adds E2E tests for the fused operation on A3 hardware.

## Technical Significance
Fusing the hc_pre operation reduces kernel launch overhead and enables more efficient memory access patterns by combining multiple operations into a single kernel. This improves inference performance for DeepSeek V4 models, particularly for the pre-head computation phase.

## Related
- `technique-operator-fusion`
- `hw-cube-unit`