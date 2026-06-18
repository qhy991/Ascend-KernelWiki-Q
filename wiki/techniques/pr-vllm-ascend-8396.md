---
id: technique-pr-vllm-ascend-8396
title: "PR Insight: vllm-project/vllm-ascend #8396"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/8396"
---

# PR Insight: vllm-project/vllm-ascend #8396

**Title:** [BugFix] Fix Qwen3.5 MoE FC1 error under high concurrency when dp>1

## Overview
This PR fixes FC1 errors in Qwen3.5 MoE models under high concurrency when data parallelism (dp) > 1. GDN (Grouped Delta Network) Attention was using FIA's query_start_loc (padded), which could cause conv1d update errors. The fix makes GDN use its own query_start_loc (unpadded) and includes comprehensive e2e testing for validation.

## Technical Significance
This fix is critical for stable Qwen3.5 MoE deployment in high-concurrency, multi-rank environments. The main branch version includes comprehensive e2e testing to validate the fix. The issue demonstrates how incorrect padding assumptions can lead to errors in attention computation when combined with conv1d operations in MoE models.

## Related
- `technique-moe-optimization`
- `technique-gdn-attention`
- `technique-high-concurrency`