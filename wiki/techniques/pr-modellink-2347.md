---
id: technique-pr-modellink-2347
title: "PR Insight: Ascend/ModelLink #2347"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - qlora
  - mixtral
  - memory-optimization
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2347"
---

# PR Insight: Ascend/ModelLink #2347

**Title:** 修复QLoRA量化权重OOM的问题，增加Mixtral-8x22B QLoRA脚本

## Overview
This PR fixes out-of-memory (OOM) issues with QLoRA quantized weights and adds QLoRA fine-tuning scripts for Mixtral-8x22B model. The fix enables training very large quantized models within available NPU memory.

## Technical Significance
QLoRA combines 4-bit quantization with LoRA adapters to dramatically reduce memory footprint. OOM issues indicate suboptimal memory management in quantized weight handling. The fix likely optimizes memory allocation, quantization/dequantization overhead, and memory access patterns. Adding Mixtral-8x22B support enables training of 141B parameter MoE models with QLoRA on Ascend hardware, making large-scale fine-tuning accessible with limited memory resources.

## Related
- `technique-qlora`
- `technique-quantization`
- `technique-moe-training`
- `technique-memory-optimization`