---
id: technique-pr-vllm-ascend-9972
title: "PR Insight: vllm-project/vllm-ascend #9972"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - mtp
  - lm-head
  - qwen3.5
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9972"
---

# PR Insight: vllm-project/vllm-ascend #9972

**Title:** [Quantization][BugFix] Fix lm_head prefix mapping for qwen3_5_moe MTP drafter

## Overview
This PR fixes lm_head prefix mapping issues for qwen3_5_moe models when using MTP (multi-token prefix) drafting. The fix ensures correct handling of lm_head in quantized MoE models during MTP draft generation.

## Technical Significance
Resolves quantization compatibility issues for qwen3_5_moe MTP drafters by fixing lm_head prefix mapping. Ensures that quantized MoE models work correctly with MTP speculative decoding, improving support for quantized MoE inference with draft models.

## Related
- `technique-quantization`, `technique-moe`, `technique-mtp`, `technique-lm-head`