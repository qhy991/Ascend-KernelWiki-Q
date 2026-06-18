---
id: technique-pr-vllm-ascend-4141
title: "PR Insight: vllm-project/vllm-ascend #4141"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - lora
  - precision
  - bugfix
  - ascendc
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4141"
---

# PR Insight: vllm-project/vllm-ascend #4141

**Title:** [BugFix]Fix precision issue for LoRA feature

## Overview
This PR fixes precision issues in the LoRA feature for vllm-ascend. The fix addresses numerical accuracy problems in LoRA kernel implementations (bgmv_expand, bgmv_shrink, sgmv_expand, sgmv_shrink) by modifying C++ kernel code and the punica_npu Python wrapper to ensure correct LoRA weight application.

## Technical Significance
LoRA precision issues can cause incorrect model outputs, defeating the purpose of parameter-efficient fine-tuning. The fix ensures that LoRA weights are applied with sufficient numerical precision to maintain model accuracy. Proper LoRA implementation is critical for production use of parameter-efficient fine-tuning on Ascend NPUs.

## Related
- `technique-lora`, `technique-ascendc`, `pattern-numerical-stability`, `technique-precision`