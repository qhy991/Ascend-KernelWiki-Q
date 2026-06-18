---
id: technique-pr-vllm-ascend-9456
title: "PR Insight: vllm-project/vllm-ascend #9456"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek-v4
  - mtp
  - async-scheduling
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9456"
---

# PR Insight: vllm-project/vllm-ascend #9456

**Title:** [BugFix]Fix Deepseek-V4 async scheduling with MTP

## Overview
This PR fixes async scheduling issues for DeepSeek V4 when using MTP (Multi-Token Prediction). The fix is implemented in the model runner to ensure proper coordination between async execution and MTP token generation.

## Technical Significance
Async scheduling is critical for maximizing GPU utilization, but requires careful coordination with MTP to ensure correctness. The fix prevents scheduling conflicts and ensures that async execution properly integrates with MTP token generation, improving both performance and reliability.

## Related
- `technique-pipeline-scheduling`
- `kernel-attention`