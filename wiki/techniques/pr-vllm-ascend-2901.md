---
id: technique-pr-vllm-ascend-2901
title: "PR Insight: vllm-project/vllm-ascend #2901"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - torchair
  - operator-replacement
  - tiling
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2901"
---

# PR Insight: vllm-project/vllm-ascend #2901

**Title:** [Bugfix]:replace npu_incre_flash_attention with npu_fused_infer_atten…

## Overview
This PR replaces the npu_incre_flash_attention operator with npu_fused_infer_attention_score in the TorchAir attention implementation to enable tiling update support. The change affects torchair_attention.py and adds comprehensive test cases.

## Technical Significance
The operator replacement enables dynamic tiling updates for attention computation, which is essential for optimizing performance across different sequence lengths and batch sizes. The npu_fused_infer_attention_score operator provides better flexibility for memory layout and tiling strategies, allowing more efficient use of Ascend's Cube unit and unified buffer.

## Related
- `kernel-attention-ascendc`, `technique-tiling`, `kernel-flash-attention`