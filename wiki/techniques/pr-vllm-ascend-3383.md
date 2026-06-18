---
id: technique-pr-vllm-ascend-3383
title: "PR Insight: vllm-project/vllm-ascend #3383"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - hccl-optimization
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3383"
---

# PR Insight: vllm-project/vllm-ascend #3383

**Title:** [Bugfix] Add quantization param for multi-node CI

## Overview
Add quantization param for `deepseek-w8a8` multi-node test

## Technical Significance
Adds quantization parameters for multi-node CI testing to ensure correct quantization behavior in distributed environments.

## Related
- `technique-quantization`
