---
id: technique-pr-vllm-ascend-10458
title: "PR Insight: vllm-project/vllm-ascend #10458"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - deepseek
  - modelslim
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10458"
---

# PR Insight: vllm-project/vllm-ascend #10458

**Title:** [Quantization][BugFix] dsv4 quant_model_substr_mapping key fix

## Overview
This PR fixes a typo in the `QUANT_MODEL_SUBSTR_MAPPINGS` dictionary for DeepSeek V4 models. Specifically, it corrects the mapping key value from `".sefl_attn."` to `".self_attn."` to ensure proper attention layer mapping during quantization. This typo would have prevented proper parameter identification and mapping during the quantization process for DeepSeek V4 models.

## Technical Significance
While this is a simple typo fix, it's critical for correct quantization of DeepSeek V4 models. The incorrect substring `".sefl_attn."` would not match the actual parameter naming pattern `".self_attn."`, causing attention layer parameters to be incorrectly handled during quantization. This could lead to incorrect quantized weights and potential accuracy degradation. The fix ensures proper parameter identification and mapping during the Modelslim quantization workflow.

## Related
- `technique-quantization`
- `technique-deepseek`
- `technique-modelslim`