---
id: technique-pr-modellink-2340
title: "PR Insight: Ascend/ModelLink #2340"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - qlora
  - mla
  - parameter-efficient-finetuning
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2340"
---

# PR Insight: Ascend/ModelLink #2340

**Title:** support qlora-tuning for LinearNoTP in MLA

## Overview
This PR adds support for QLoRA (Quantized LoRA) fine-tuning for LinearNoTP operations within the MLA (Multi-Head Latent Attention) component. This enables parameter-efficient fine-tuning with quantization on the MLA projection layers.

## Technical Significance
QLoRA combines quantization (typically 4-bit) with LoRA adapters to dramatically reduce memory requirements for fine-tuning. Supporting this for MLA's LinearNoTP operations (linear layers without tensor parallelism) enables efficient fine-tuning of DeepSeekV3 models on memory-constrained Ascend NPUs. The quantization must preserve MLA's compressed KV representation accuracy while enabling large-scale fine-tuning tasks.

## Related
- `kernel-attention-mla`
- `technique-qlora`
- `technique-quantization`