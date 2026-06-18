---
id: technique-pr-vllm-ascend-6393
title: "PR Insight: vllm-project/vllm-ascend #6393"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kernel
  - dispatch
  - gmm
  - nd-format
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6393"
---

# PR Insight: vllm-project/vllm-ascend #6393

**Title:** [Feature] DispatchGmmCombineDecode support bf16/float16 gmm1/gmm2 weight and support gmm weight with ND format

## Overview
This PR extends the DispatchGmmCombineDecode operator to support bf16/float16 weight data types (previously only W8A8) and ND data format for gmm1_weight and gmm2_weight inputs (previously only NZ format). The changes include new epilogue kernels and tiling logic in the AscendC implementation.

## Technical Significance
The expansion enables non-W8A8 quantization scenarios and reduces format conversion overhead by supporting ND format directly. This improves flexibility for different quantization schemes and eliminates unnecessary format conversion kernels.

## Related
- `technique-dispatch`
- `technique-gmm`
- `technique-nd-format`
- `technique-nz-format`