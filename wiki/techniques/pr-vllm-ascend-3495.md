---
id: technique-pr-vllm-ascend-3495
title: "PR Insight: vllm-project/vllm-ascend #3495"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/3495"
---

# PR Insight: vllm-project/vllm-ascend #3495

**Title:** [Feat] Shared expert dp for deepseek and deepseek_mtp

## Overview
shared expert dp for deepseek and deepseek_mtp, could be combined with sp to improve performance.

## Technical Significance
Implements shared expert data parallelism for DeepSeek and DeepSeek MTP models to reduce communication overhead.

## Related
- `hw-cube-unit`
- `technique-speculative-decoding`
