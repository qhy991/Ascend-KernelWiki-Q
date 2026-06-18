---
id: technique-pr-vllm-ascend-2672
title: "PR Insight: vllm-project/vllm-ascend #2672"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - lora
  - ascendc
  - custom-op
  - accuracy
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2672"
---

# PR Insight: vllm-project/vllm-ascend #2672

**Title:** [Bugfix][LoRA][Operator] Fix LoRA custom operators accuracy issue

## Overview
This PR fixes accuracy issues in LoRA custom AscendC operators (bgmv_shrink, sgmv_shrink, bgmv_expand, sgmv_expand). The bug was caused by incorrect usage of GlobalTensor.GetSize() without properly passing the bufferSize parameter to GlobalTensor.SetGlobalBuffer().

## Technical Significance
The accuracy fix resolves a critical LoRA inference correctness issue. According to AscendC API documentation, GlobalTensor.GetSize() returns random values if GlobalTensor.SetGlobalBuffer() is not called with the bufferSize parameter first. The fix updates all four custom operators to properly set buffer sizes before querying size, ensuring correct LoRA behavior.

## Related
- `technique-lora`
- `technique-ascendc`
- `technique-custom-op`