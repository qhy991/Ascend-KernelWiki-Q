---
id: technique-pr-vllm-ascend-8387
title: "PR Insight: vllm-project/vllm-ascend #8387"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
  - ascend310p
tags:
  - attention
  - bugfix
  - atten-mask
  - npu-fused-infer-attention-score-v2
  - parameter
  - ascende
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8387"
---

# PR Insight: vllm-project/vllm-ascend #8387

**Title:** [Attention][BugFix] Fix the atten_mask in the npu_fused_infer_attention_score_v2

## Overview
This PR fixes an input parameter error in the npu_fused_infer_attention_score_v2 operator. The fix adapts to the operator's input parameter constraints by correcting the attention mask parameter handling. The changes affect both main branch and 310P-specific implementations to ensure consistent behavior across hardware platforms.

## Technical Significance
Correct attention mask parameter passing is critical for attention computation accuracy and performance. The fix ensures compatibility with the NPU operator's API constraints, preventing potential crashes or incorrect results. This PR demonstrates the importance of aligning with hardware operator specifications when using fused attention implementations.

## Related
- `technique-attention-optimization`
- `technique-operator-compatibility`
- `hw-ascend310p`