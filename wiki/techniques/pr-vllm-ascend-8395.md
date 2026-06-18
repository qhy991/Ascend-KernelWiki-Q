---
id: technique-pr-vllm-ascend-8395
title: "PR Insight: vllm-project/vllm-ascend #8395"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - gdn
  - qwen3.5
  - bugfix
  - high-concurrency
  - conv1d
  - dp
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8395"
---

# PR Insight: vllm-project/vllm-ascend #8395

**Title:** [v0.18.0][BugFix] Fix Qwen3.5 MoE FC1 error under high concurrency when dp>1

## Overview
This PR fixes FC1 errors in Qwen3.5 MoE models under high concurrency when data parallelism (dp) > 1. GDN (Grouped Delta Network) Attention was using FIA's query_start_loc (padded), which could cause conv1d update errors. The fix makes GDN use its own query_start_loc (unpadded) to avoid these issues in high-concurrency scenarios.

## Technical Significance
This fix is critical for stable Qwen3.5 MoE deployment in high-concurrency, multi-rank environments. The issue demonstrates how incorrect padding assumptions can lead to errors in attention computation when combined with conv1d operations. The PR highlights the importance of using correct location tracking for different attention components in MoE models.

## Related
- `technique-moe-optimization`
- `technique-gdn-attention`
- `technique-high-concurrency`