---
id: technique-pr-vllm-ascend-1884
title: "PR Insight: vllm-project/vllm-ascend #1884"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - lora
  - custom-kernels
  - bgmv
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1884"
---

# PR Insight: vllm-project/vllm-ascend #1884

**Title:** Add Custom Kernels For LoRA Performance

## Overview
This PR adds two custom AscendC kernels (bgmv_shrink and bgmv_expand) to optimize LoRA (Low-Rank Adaptation) performance. Testing on Qwen2.5 7B shows approximately 70% improvement in TTFT, TPOT, and throughput.

## Technical Significance
Major performance optimization for LoRA workloads. The custom BGMV (Batch Grouped MatMul with Vector) kernels are specifically optimized for the LoRA pattern, which involves multiplying low-rank adapter matrices with activations.

## Related
- `kernel-bgmv-ascendc`
- `technique-lora`
- `technique-custom-kernels`