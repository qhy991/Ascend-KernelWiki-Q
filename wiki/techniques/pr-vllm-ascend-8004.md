---
id: technique-pr-vllm-ascend-8004
title: "PR Insight: vllm-project/vllm-ascend #8004"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - mtp
  - flash-comm
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8004"
---

# PR Insight: vllm-project/vllm-ascend #8004

**Title:** [v0.18.0][BugFix] Fix Qwen3.5 MoE flash comm v1 shared expert shape error of mtp layer on A2

## Overview
This PR fixes a shape error that occurs in Qwen3.5 MoE models when flash communication v1 is enabled, specifically affecting the MTP (Multi-Token Prediction) layer's shared expert processing on A2 hardware. The fix adjusts shape handling in the custom operator registration and spec decode proposer.

## Technical Significance
MoE models with flash communication rely on correct tensor shapes for expert dispatch and combine operations. The shape error in MTP layers would cause incorrect execution or crashes. The fix ensures proper shape handling for shared experts in flash comm v1 scenarios, enabling correct Qwen3.5 MoE MTP inference on Ascend hardware.

## Related
- `kernel-moe`
- `pattern-moe-dispatch`
- `pattern-mtp`
- `technique-hccl-optimization`