---
id: technique-pr-vllm-ascend-925
title: "PR Insight: vllm-project/vllm-ascend #925"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - qwen3
  - w8a8
  - model-support
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/925"
---

# PR Insight: vllm-project/vllm-ascend #925

**Title:** [Feature] Add CustomQwen3MoeForCausalLM model

## Overview
This PR adds CustomQwen3MoeForCausalLM model by tweaking packed_modules_mapping to support W8A8 quantized weights. The custom model class enables proper weight packing for quantized MoE models.

## Technical Significance
W8A8 quantization requires special weight packing optimizations. The custom model class ensures that Qwen3-MoE models can leverage W8A8 quantization benefits while maintaining correct weight organization for efficient computation on Ascend hardware.

## Related
- `kernel-moe`
- `kernel-qwen3`
- `technique-w8a8`