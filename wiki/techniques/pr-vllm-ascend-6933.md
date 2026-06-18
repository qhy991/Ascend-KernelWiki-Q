---
id: technique-pr-vllm-ascend-6933
title: "PR Insight: vllm-project/vllm-ascend #6933"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen
  - moe
  - triton
  - gdn
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6933"
---

# PR Insight: vllm-project/vllm-ascend #6933

**Title:** [fix] Add support for Qwen3.5 Dense and MoE on Ascend

## Overview
Adds support for Qwen3.5 MoE models on Ascend devices by adding quantization configuration with prefix mappings and packed module definitions for ModelSlim quantization. Also fixes a bug in the `fused_gdn_gating` Triton kernel where the `BLK_BATCHES` calculation had operator precedence issues and potential out-of-bounds memory access.

## Technical Significance
Enables correct and efficient execution of Qwen3.5 MoE models on Ascend hardware by fixing critical Triton kernel bugs and adding proper quantization support. The GDN kernel fix includes clamping to prevent unified buffer overflow and robust calculation improvements.

## Related
- `technique-moe`, `technique-gdn`, `technique-triton`, `technique-qwen`