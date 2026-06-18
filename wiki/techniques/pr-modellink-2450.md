---
id: technique-pr-modellink-2450
title: "PR Insight: Ascend/ModelLink #2450"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - lora
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2450"
---

# PR Insight: Ascend/ModelLink #2450

**Title:** only convert lora ckpt to hf

## Overview
This PR refines the LoRA checkpoint conversion logic to focus specifically on LoRA weights, rather than full model weights. It improves the efficiency and focus of the conversion pipeline when working with LoRA-fine-tuned models.

## Technical Significance
Optimizes the conversion process by avoiding unnecessary full-model weight processing when only LoRA adapter weights are needed for deployment, reducing memory overhead and conversion time.

## Related
- `technique-lora` / `technique-weight-conversion`