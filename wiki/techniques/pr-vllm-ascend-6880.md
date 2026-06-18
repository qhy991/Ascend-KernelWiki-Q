---
id: technique-pr-vllm-ascend-6880
title: "PR Insight: vllm-project/vllm-ascend #6880"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - rope
  - rotary-embedding
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6880"
---

# PR Insight: vllm-project/vllm-ascend #6880

**Title:** [bugs] fix pass bug: pass really rope dim for npu_rotary_embedding

## Overview
Fixes a bug in the QKNorm-RoPE fusion pass where incorrect RoPE dimension was passed to `npu_rotary_embedding` operator. The fix changes the parameter from `self.head_dim` to `self.rope_dim` to ensure correct rotary embedding computation.

## Technical Significance
Corrects rotary embedding calculations by using the actual RoPE dimension instead of the head dimension, ensuring accurate positional encoding for attention mechanisms. This fix is critical for models where RoPE dimension differs from head dimension.

## Related
- `technique-rope`, `technique-rotary-embedding`, `technique-operator-fusion`