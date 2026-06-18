---
id: technique-pr-modellink-2386
title: "PR Insight: Ascend/ModelLink #2386"
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
  - "https://gitee.com/ascend/ModelLink/pulls/2386"
---

# PR Insight: Ascend/ModelLink #2386

**Title:** 修复LinearNoTP不支持QLoRA微调的问题

## Overview
This PR fixes an issue where LinearNoTP (likely a tensor parallelism bypass mode) did not support QLoRA fine-tuning, enabling quantized parameter-efficient fine-tuning in this mode.

## Technical Significance
Enabling QLoRA in LinearNoTP mode provides flexibility for training scenarios where tensor parallelism is bypassed, ensuring memory-efficient fine-tuning works across different parallelization configurations.

## Related
- `technique-lora` / `technique-qlora` / `technique-tensor-parallel` / `technique-linear-notp`