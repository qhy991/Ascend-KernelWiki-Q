---
id: technique-pr-vllm-ascend-7748
title: "PR Insight: vllm-project/vllm-ascend #7748"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - modelslim
  - compressed-tensors
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7748"
---

# PR Insight: vllm-project/vllm-ascend #7748

**Title:** [v0.18.0][Bugfix]Fix Error "AttributeError: 'AscendCompressedTensorsConfig' obiect has no attribute 'enabling_fa_quant'"

## Overview
This PR fixes an AttributeError in AscendCompressedTensorsConfig by adding the missing 'enabling_fa_quant' attribute for v0.18.0. The fix affects MLA v1 attention, quantization utilities, and model runner.

## Technical Significance
Resolves configuration errors in compressed tensors quantization for v0.18.0, ensuring proper attribute initialization for flash attention quantization support in ModelSlim configurations.

## Related
- `technique-quantization`, `kernel-mla`, `pattern-compressed-tensors`, `technique-modelslim-config`, `pattern-fa-quantization`