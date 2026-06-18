---
id: technique-pr-modellink-2449
title: "PR Insight: Ascend/ModelLink #2449"
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
  - "https://gitee.com/ascend/ModelLink/pulls/2449"
---

# PR Insight: Ascend/ModelLink #2449

**Title:** 增加lora微调时的swap-attn和RMS融合算子的限制

## Overview
This PR adds restrictions or conditions for using swap-attention and RMSNorm fusion operators during LoRA fine-tuning, preventing issues when these optimizations conflict with LoRA's parameter-efficient approach.

## Technical Significance
Prevents incorrect application of aggressive optimization techniques that may break LoRA's low-rank adaptation semantics, ensuring numerical correctness while maintaining performance where compatible.

## Related
- `technique-lora` / `technique-operator-fusion` / `technique-rmsnorm`