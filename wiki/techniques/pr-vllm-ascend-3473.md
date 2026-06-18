---
id: technique-pr-vllm-ascend-3473
title: "PR Insight: vllm-project/vllm-ascend #3473"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - moe
  - hccl-optimization
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3473"
---

# PR Insight: vllm-project/vllm-ascend #3473

**Title:** [BugFix]Support redundant experts in EPLB

## Overview
This PR [bugfix]support redundant experts in eplb. It modifies core implementation files including vllm_ascend/eplb/core/eplb_utils.py, vllm_ascend/ops/moe/experts_selector.py, vllm_ascend/ops/moe/token_dispatcher.py.

## Technical Significance
Supports redundant experts in EPLB (Expert Parallel Load Balancing) for improved MoE robustness and load distribution.

## Related
- `technique-moe-routing`
