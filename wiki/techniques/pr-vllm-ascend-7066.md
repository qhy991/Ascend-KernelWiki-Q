---
id: technique-pr-vllm-ascend-7066
title: "PR Insight: vllm-project/vllm-ascend #7066"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen
  - moe
  - operator-fusion
  - bf16
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7066"
---

# PR Insight: vllm-project/vllm-ascend #7066

**Title:** [bugfix]Enable dispatch_ffn_combine feature for qwen3.5

## Overview
Enables `dispatch_ffn_combine` fusion operator for Qwen3.5 MoE models. The fix addresses the problem where the operator failed to activate in W8A8 quantization scenarios due to missing quantize field in config.json, and extends support to BF16 scenarios beyond the original `quant_type == "w8a8_dynamic"` condition.

## Technical Significance
Activates operator fusion for Qwen3.5 MoE in both quantized and BF16 scenarios, improving performance by leveraging the `dispatch_ffn_combine` fusion operator. The fix removes overly restrictive activation conditions and enables fusion in valid BF16 cases.

## Related
- `technique-moe`, `technique-operator-fusion`, `technique-qwen`, `technique-bf16`