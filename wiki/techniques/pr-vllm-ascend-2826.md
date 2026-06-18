---
id: technique-pr-vllm-ascend-2826
title: "PR Insight: vllm-project/vllm-ascend #2826"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - mla
  - custom-op
  - deepseek
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2826"
---

# PR Insight: vllm-project/vllm-ascend #2826

**Title:** [CustomOp] Register AscendMultiHeadLatentAttention instead of overwrite forward

## Overview
This PR changes the registration approach for AscendMultiHeadLatentAttention (MLA) from overriding forward methods to proper custom operator registration. It affects the DeepSeek V2 model implementation and MLA layer utilities.

## Technical Significance
Refactoring from forward method overriding to proper custom operator registration improves integration with vLLM's operator framework and enables better optimization opportunities. This approach is more maintainable and allows for proper graph compilation and optimization in aclgraph mode. MLA is a key attention variant used in DeepSeek V2 for reducing memory footprint.

## Related
- `kernel-attention-ascendc`, `technique-mla`, `kernel-deepseek`