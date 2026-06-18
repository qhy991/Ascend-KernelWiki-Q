---
id: technique-pr-vllm-ascend-4999
title: "PR Insight: vllm-project/vllm-ascend #4999"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mlp-tp
  - dense-ffn
  - moe
  - deepseek
  - chatglm
  - tensor-parallelism
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4999"
---

# PR Insight: vllm-project/vllm-ascend #4999

**Title:** [Feat] Support MLP_TP feature, exclude MOE layer

## Overview
This PR implements MLP tensor parallelism for dense FFN layers in models that have both MLP and MoE layers (e.g., DeepSeek, ChatGLM). It adds an is_moe_layer function to mlp_tp to selectively apply TP only to non-MoE layers, enabling the first three layers of DeepSeek models to use dense FFN TP.

## Technical Significance
Enables mixed parallelism where early model layers use dense MLP-TP while later layers use MoE. The is_moe_layer check ensures TP is only applied to dense FFN, avoiding conflicts with MoE's expert parallelism.

## Related
- `technique-tensor-parallelism`
- `kernel-mlp-tp`
- `kernel-moe`
- `kernel-deepseekv3`
- `kernel-chatglm`