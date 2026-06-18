---
id: technique-pr-vllm-ascend-5040
title: "PR Insight: vllm-project/vllm-ascend #5040"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - dispatch-gmm-combine-decode
  - mc2
  - operator-fusion
  - w8a8
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5040"
---

# PR Insight: vllm-project/vllm-ascend #5040

**Title:** [Feature]Use DispatchGmmCombineDecode operator to replace MC2(Optional)

## Overview
This PR adds optional model-side integration for the AscendC DispatchGmmCombineDecode operator for MoE decoding. When VLLM_ASCEND_ENABLE_FUSED_MC2=2, the multi-operator MC2 path (A8W8 dispatch → GMM → SwiGLU → GMM → combine) can be replaced by the single fused DispatchGmmCombineDecode operator. By default, the existing MC2 implementation is preserved.

## Technical Significance
Enables experimental use of a highly fused MoE operator that combines multiple operations (dispatch, GMM, SwiGLU, combine) into a single kernel for improved performance. The optional flag allows users to test the new operator while maintaining the stable existing implementation as the default.

## Related
- `kernel-dispatch-gmm-combine-decode`
- `kernel-mc2`
- `kernel-gmm`
- `kernel-swiglu`
- `technique-moe-fusion`