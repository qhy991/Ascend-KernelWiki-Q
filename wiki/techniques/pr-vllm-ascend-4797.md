---
id: technique-pr-vllm-ascend-4797
title: "PR Insight: vllm-project/vllm-ascend #4797"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - moe
  - deepseekv3
  - w8a8-dynamic
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4797"
---

# PR Insight: vllm-project/vllm-ascend #4797

**Title:** [bugfix] Fixed the bug in retrieving the quantization method for mlp.…

## Overview
This PR fixes a bug in retrieving quantization methods for MoE MLP layers in eager mode. The quantization file uses per-expert naming (e.g., `model.layers.3.mlp.experts.255.gate_proj.weight`) but the code was looking for the generic `model.layers.3.mlp.experts.weight`, causing a KeyError.

## Technical Significance
Fixes quantization config lookup to handle per-expert weight naming in DeepSeek V3.2 MoE models. Ensures W8A8_DYNAMIC quantization is correctly applied to each expert's gate_proj, down_proj, and up_proj weights.

## Related
- `technique-w8a8-quantization`
- `kernel-moe-mlp`
- `kernel-deepseekv3`
- `technique-quant-config`