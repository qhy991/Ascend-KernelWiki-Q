---
id: technique-pr-modellink-2319
title: "PR Insight: Ascend/ModelLink #2319"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - moe
  - weight-conversion
  - deepseek3
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2319"
---

# PR Insight: Ascend/ModelLink #2319

**Title:** deepseek3权重hf转mg支持moe_tp_extend_ep

## Overview
Adds support for MoE tensor parallelism with expert parallelism extension during HuggingFace to Megatron weight conversion for DeepSeek3. This enables proper weight transformation for DeepSeek3's MoE architecture when using combined TP and EP strategies.

## Technical Significance
Enables training of DeepSeek3's large MoE architecture on Ascend hardware by supporting advanced parallelism strategies during weight conversion. The combination of TP and EP is crucial for efficiently scaling MoE models across multiple NPU devices.

## Related
- technique-moe
- technique-hccl-optimization
- technique-data-reuse