---
id: technique-pr-vllm-ascend-9432
title: "PR Insight: vllm-project/vllm-ascend #9432"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascend950
  - gmm-swiglu-quant
  - reshape-and-cache
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9432"
---

# PR Insight: vllm-project/vllm-ascend #9432

**Title:** [BugFix][Ascend950]Fixup GMM_swiglu_quant and reshape_and_cache on 950

## Overview
This PR fixes issues with the GMM_swiglu_quant operation and reshape_and_cache functionality on Ascend 950 hardware. The changes are in the device operator layer and MoE MLP implementation to ensure correct behavior on 950.

## Technical Significance
Ascend 950 has different hardware characteristics than earlier generations, requiring specific fixes for quantization and caching operations. These fixes ensure reliable inference of quantized MoE models on the latest Ascend hardware.

## Related
- `kernel-moe`
- `technique-quantization`