---
id: technique-pr-vllm-ascend-4516
title: "PR Insight: vllm-project/vllm-ascend #4516"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - quantization
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4516"
---

# PR Insight: vllm-project/vllm-ascend #4516

**Title:** [Feat] Support native Kimi-K2-Thinking native W4A16 quantized experts weights

**Author:** zhoux77899 | **Merged:** 2025-12-10

## Overview
Adds support for new quantization schemes including W8A16 and Kimi-K2-Thinking W4A16 quantized experts. Enables more memory-efficient inference with minimal accuracy loss. The implementation extends existing quantization frameworks to handle new weight formats.

## Technical Significance
MoE operations benefit from improved load balancing and expert routing efficiency. Changes affect how expert weights are loaded and distributed, reducing communication overhead and improving parallelism. These optimizations are crucial for scaling MoE models on Ascend NPU clusters.

## Related
- `kernel-moe-ascendc`
- `technique-quantization`
