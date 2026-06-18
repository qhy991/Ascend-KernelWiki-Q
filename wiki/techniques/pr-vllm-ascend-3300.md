---
id: technique-pr-vllm-ascend-3300
title: "PR Insight: vllm-project/vllm-ascend #3300"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - hccl-optimization
  - speculative-decoding
  - decode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3300"
---

# PR Insight: vllm-project/vllm-ascend #3300

**Title:** bugfix for mtp

## Overview
when mtp>1, we need refresh cos ans sin in each step.

## Technical Significance
Fixes MTP-related bugs to improve stability and correctness of speculative decoding in multi-token prediction scenarios.

## Related
- `hw-cube-unit`
- `technique-speculative-decoding`
