---
id: technique-pr-modellink-2358
title: "PR Insight: Ascend/ModelLink #2358"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - lora
  - qlora
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2358"
---

# PR Insight: Ascend/ModelLink #2358

**Title:** cc-qlora support

## Overview
This PR adds support for CC-QLoRA (likely a specific variant or configuration of QLoRA), expanding the framework's quantized fine-tuning capabilities for different training scenarios.

## Technical Significance
QLoRA support enables memory-efficient fine-tuning of large models by quantizing base model weights; CC-QLoRA variant support provides additional flexibility for different hardware configurations or training objectives.

## Related
- `technique-lora` / `technique-qlora` / `technique-quantization`