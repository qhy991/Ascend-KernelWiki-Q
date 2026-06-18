---
id: technique-pr-vllm-ascend-3279
title: "PR Insight: vllm-project/vllm-ascend #3279"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - hccl-optimization
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3279"
---

# PR Insight: vllm-project/vllm-ascend #3279

**Title:** [bugfix] Fix moe bug: allgather error.

## Overview
This PR [bugfix] fix moe bug: allgather error.. It modifies core implementation files including vllm_ascend/ops/moe/token_dispatcher.py.

## Technical Significance
Fixes MoE (Mixture-of-Experts) allgather communication errors that occur during distributed expert routing and token dispatch.

## Related
- `technique-moe-routing`
