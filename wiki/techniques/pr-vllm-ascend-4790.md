---
id: technique-pr-vllm-ascend-4790
title: "PR Insight: vllm-project/vllm-ascend #4790"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - dispatch-gmm-combine-decode
  - matmul
  - swiglu
  - dequant
  - ascendc
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4790"
---

# PR Insight: vllm-project/vllm-ascend #4790

**Title:** [kernel] Adapt DispatchGmmCombineDecode operator to parameters of small operators

## Overview
This PR adapts the DispatchGmmCombineDecode operator to use the same parameters (weights and scales) as small operators. The changes eliminate the need to permute weights/scales of GMM1 and transpose weights of GMM2, enabling shared parameter usage for better model adaptation.

## Technical Significance
Simplifies parameter handling in the grouped matrix multiplication combine decode operator by removing weight permutation and transpose requirements. This allows the AscendC kernel to directly use the same weights/scales as small operators, reducing preprocessing overhead and improving model compatibility.

## Related
- `kernel-dispatch-gmm-combine-decode`
- `kernel-grouped-matmul`
- `technique-dequantization`
- `kernel-swiglu`