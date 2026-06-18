---
id: technique-pr-vllm-ascend-3509
title: "PR Insight: vllm-project/vllm-ascend #3509"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - operator-fusion
  - hccl-optimization
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3509"
---

# PR Insight: vllm-project/vllm-ascend #3509

**Title:** Add mrope op fusion

## Overview
Add mrope fusion op for qwen2.5-vl. This mrope operator dosen't support Qwen3-VL currently. Thus could only take affect in qwen2.5-vl

## Technical Significance
Adds mrope (multi-dimensional RoPE) operator fusion for improved attention computation efficiency.

## Related
- `technique-operator-fusion`
