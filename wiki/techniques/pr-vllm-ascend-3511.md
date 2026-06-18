---
id: technique-pr-vllm-ascend-3511
title: "PR Insight: vllm-project/vllm-ascend #3511"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/3511"
---

# PR Insight: vllm-project/vllm-ascend #3511

**Title:** [Patch]patch of v1 executor when enable eplb.

## Overview
when using dynamic eplb, patch v1 executor to avoid create child process failed.

## Technical Significance
Applies patch for v1 executor when enabling EPLB to ensure correct MoE behavior.

## Related
- `technique-moe-routing`
