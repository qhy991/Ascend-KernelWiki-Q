---
id: technique-pr-sgl-kernel-npu-282
title: "PR Insight: sgl-project/sgl-kernel-npu #282"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qkv
  - rmsnorm
  - rope
  - llama
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/282"
---

# PR Insight: sgl-project/sgl-kernel-npu #282

**Title:** modify split_qkv_rmsnorm_rope

## Overview
Modifies the split_qkv_rmsnorm_rope operation to make normalization optional, enabling support for LLaMA models that may not require the normalization step.

## Technical Significance
Different model architectures have varying requirements for QKV processing. Making normalization optional provides flexibility to support multiple model families including LLaMA, ensuring the operator can be used across different architectures without unnecessary computation overhead.

## Related
- `wiki-technique-qkv-splitting`
- `wiki-technique-rmsnorm`
- `wiki-technique-rope`
- `wiki-technique-model-adaptation`