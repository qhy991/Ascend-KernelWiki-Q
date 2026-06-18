---
id: technique-pr-vllm-ascend-9671
title: "PR Insight: vllm-project/vllm-ascend #9671"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - moe
  - quantization
  - mxfp8
  - flashcomm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9671"
---

# PR Insight: vllm-project/vllm-ascend #9671

**Title:** [Ascend950][Feature]Support MXFP8 FlashcommV3 on 950

## Overview
This PR adds support for MXFP8 quantization with FlashCommV3 on Ascend 950. It updates the W8A8_MXFP8 MoE path to reuse `topk_weights` and `topk_ids` from `FlashCommon3Context` when `multistream_overlap_gate` is enabled, avoiding redundant `select_experts` calls.

## Technical Significance
Enables MXFP8 MoE execution to work with FlashCommV3's multistream overlap on Ascend 950, eliminating duplicate gating computation. Improves QPS from 0.62 to 0.64 in DeepSeek V3.1 prefill scenarios on Ascend 950, demonstrating performance benefits from overlap optimization.

## Related
- `technique-moe`, `technique-quantization`, `kernel-matmul`