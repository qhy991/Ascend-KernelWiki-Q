---
id: technique-pr-vllm-ascend-8675
title: "PR Insight: vllm-project/vllm-ascend #8675"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/8675"
---

# PR Insight: vllm-project/vllm-ascend #8675

**Title:** [BugFix] Revert change of `balance_flag` to fix DSV3.1 W4A8 TTFT degradation

## Overview
This PR fixes TTFT degradation on DeepSeek-V3.1 with W4A8 quantization by reverting changes to `balance_flag` that were introduced in PR #7611. This is a duplicate fix to #8674 but for the v0.19.0 version, modifying the same file `patch_balance_schedule.py` to restore the previous scheduling behavior.

## Technical Significance
This fix demonstrates the same performance regression issue addressed in #8674, indicating that the scheduling change affected multiple vLLM versions. The consistent fix across versions confirms that `balance_flag` modifications had adverse effects on W4A8 quantized DeepSeek-V3.1 models' TTFT performance, highlighting the sensitivity of load balancing heuristics to specific model characteristics.

## Related
- `technique-pipeline-scheduling`
- `technique-double-buffering`
- `kernel-matmul-ascendc`