---
id: technique-pr-vllm-ascend-6103
title: "PR Insight: vllm-project/vllm-ascend #6103"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3vl
  - quantization
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6103"
---

# PR Insight: vllm-project/vllm-ascend #6103

**Title:** [0.13.0][cherry-pick][BugFix] fix 3vl dense model load quant weight

## Overview
This is a cherry-pick of PR #6100 for the v0.13.0 release branch. It fixes the same weight loading error for Qwen3VL dense quantization models, ensuring successful model initialization and inference.

## Technical Significance
This fix ensures the v0.13.0 branch can deploy quantized Qwen3VL vision-language models. The cherry-pick applies the same weight loading fix, enabling correct initialization of dense quantization variants with reduced memory footprint.

## Related
- `technique-pr-vllm-ascend-6100`, `technique-qwen3vl`, `technique-quantization`