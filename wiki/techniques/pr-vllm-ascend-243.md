---
id: technique-pr-vllm-ascend-243
title: "PR Insight: vllm-project/vllm-ascend #243"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - api
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/243"
---

# PR Insight: vllm-project/vllm-ascend #243

**Title:** [Feature] Modify description and api for ascend quantization

## Overview
This PR refactors Ascend quantization APIs to align with vLLM naming conventions, renames AscendQKVQuantAttentionMethod to AscendKVCacheMethod, adds class documentation, and modifies weight creation processes to use get_weight/get_pertensor_param/get_perchannel_param APIs.

## Technical Significance
API consistency and documentation improvements for the quantization framework. The rename aligns with vLLM's BaseKVCacheMethod naming. The weight creation refactoring likely improves weight loading efficiency for quantized models.

## Related
- technique-quantization