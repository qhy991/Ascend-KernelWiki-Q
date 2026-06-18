---
id: technique-pr-vllm-ascend-2847
title: "PR Insight: vllm-project/vllm-ascend #2847"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - rotary-embedding
  - bugfix
  - triton
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2847"
---

# PR Insight: vllm-project/vllm-ascend #2847

**Title:** fix bug when rotary_dim is not 128

## Overview
This PR fixes a bug in rotary embedding support when rotary_dim is not 128, which was causing errors when running GLM models. The torch_npu.npu_apply_rotary_pos_emb function had limitations on supported dimensions.

## Technical Significance
Bug fix for rotary embedding with non-standard dimensions. Many models use rotary_dim values other than 128, and the previous limitation prevented these models from running correctly. This fix extends compatibility to models with various rotary dimension configurations, which is essential for supporting diverse model architectures.

## Related
- `kernel-rotary-embedding`, `technique-positional-encoding`