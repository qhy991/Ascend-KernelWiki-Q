---
id: technique-pr-vllm-ascend-8674
title: "PR Insight: vllm-project/vllm-ascend #8674"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - w4a8
  - bugfix
  - ttft
  - deepseek-v3
  - scheduling
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8674"
---

# PR Insight: vllm-project/vllm-ascend #8674

**Title:** [v0.18.0][BugFix] Fix DSV3.1 W4A8 TTFT degradation

## Overview
This PR fixes TTFT (Time To First Token) degradation on DeepSeek-V3.1 with W4A8 quantization by reverting a change to `balance_flag` that was introduced in PR #7611. The fix is targeted at the balance scheduling patch in `patch_balance_schedule.py`, restoring the previous behavior that prevented performance regression.

## Technical Significance
TTFT degradation is critical for user experience as it directly affects response latency. The `balance_flag` parameter controls scheduling decisions in the NPU execution pipeline. The reversion indicates that the original change, while potentially beneficial for some workloads, caused performance regression for W4A8 quantized DeepSeek-V3.1 models, demonstrating the need for careful performance validation across different model architectures and quantization schemes.

## Related
- `technique-pipeline-scheduling`
- `technique-double-buffering`
- `kernel-matmul-ascendc`