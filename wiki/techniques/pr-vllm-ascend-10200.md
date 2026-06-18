---
id: technique-pr-vllm-ascend-10200
title: "PR Insight: vllm-project/vllm-ascend #10200"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - flash-attention
  - multimodal
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10200"
---

# PR Insight: vllm-project/vllm-ascend #10200

**Title:** [BugFix] Preserve FP32 MM encoder attention support

## Overview
This PR restores dtype-aware operator selection for multimodal encoder attention. Previously, PR #8671 switched A2/A3 multimodal encoder attention from `npu_fusion_attention` to `_npu_flash_attention_unpad` for performance, but the unpadded operator does not support FP32 inputs, which regressed FP32 vision encoders like SigLIP. This fix implements dtype-aware dispatch: using `npu_fusion_attention` for FP32 multimodal encoder attention while keeping `_npu_flash_attention_unpad` for FP16 and BF16 to preserve the performance improvements.

## Technical Significance
This PR demonstrates the importance of operator selection based on input data types when optimizing for performance on Ascend. The `_npu_flash_attention_unpad` operator offers better performance but has dtype limitations, while `npu_fusion_attention` provides broader dtype support. The fix maintains the performance benefits for FP16/BF16 workloads while restoring correctness for FP32 vision encoders. This pattern is crucial for multimodal inference where different components may require different precision levels.

## Related
- `technique-flash-attention`
- `technique-operator-selection`
- `technique-multimodal-inference`