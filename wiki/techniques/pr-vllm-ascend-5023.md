---
id: technique-pr-vllm-ascend-5023
title: "PR Insight: vllm-project/vllm-ascend #5023"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - moe-mlp
  - precision
  - cumsum
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5023"
---

# PR Insight: vllm-project/vllm-ascend #5023

**Title:** [Bugfix]Fix precision issues in moe_mlp (vllm-ascend v0.11.0-dev)

## Overview
This PR fixes precision issues in moe_mlp (v0.11.0-dev) by using group_list[0] to replace group_diff[0] in the cumsum_group_list function, correcting the logic for converting cumsum to count format.

## Technical Significance
Resolves precision bugs in quantized MoE MLP on the v0.11.0-dev branch. Ensures correct cumsum-to-count conversion for quantization operators.

## Related
- `kernel-moe-mlp`
- `technique-quantization`
- `kernel-fused-moe`