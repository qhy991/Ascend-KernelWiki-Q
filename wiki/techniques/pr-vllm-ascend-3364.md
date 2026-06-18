---
id: technique-pr-vllm-ascend-3364
title: "PR Insight: vllm-project/vllm-ascend #3364"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - nz-format
  - quantization
  - moe
  - hccl-optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3364"
---

# PR Insight: vllm-project/vllm-ascend #3364

**Title:** [BugFix]Fix eplb problems when using dynamic eplb.

## Overview
When using dynamic eplb,it will be blocking by nz tensor.We fix these prolems by clone src tensor and recv tensor.

## Technical Significance
Fixes Expert Parallel Load Balancing (EPLB) problems when using dynamic EPLB for improved expert routing efficiency.

## Related
- `technique-moe-routing`
- `technique-nz-tiling`
