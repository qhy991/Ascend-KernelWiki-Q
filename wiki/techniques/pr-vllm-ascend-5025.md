---
id: technique-pr-vllm-ascend-5025
title: "PR Insight: vllm-project/vllm-ascend #5025"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/5025"
---

# PR Insight: vllm-project/vllm-ascend #5025

**Title:** [Bugfix] Fix precision issues in moe_mlp (vllm-ascend main)

## Overview
This PR fixes precision issues in moe_mlp (main branch) by using group_list[0] to replace group_diff[0] in the cumsum_group_list function, correcting the logic for converting cumsum to count format. This is the main branch version of PR #5023.

## Technical Significance
Resolves precision bugs in quantized MoE MLP. Ensures correct cumsum-to-count conversion for quantization operators on the main branch.

## Related
- `kernel-moe-mlp`
- `technique-quantization`
- `kernel-fused-moe`