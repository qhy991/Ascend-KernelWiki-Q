---
id: technique-pr-modellink-2407
title: "PR Insight: Ascend/ModelLink #2407"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - lora
  - gradient
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2407"
---

# PR Insight: Ascend/ModelLink #2407

**Title:** main_grad not found bugfix for lora

## Overview
This PR fixes a bug where main_grad was not found in the LoRA (Low-Rank Adaptation) implementation. LoRA is a parameter-efficient fine-tuning technique that adapts models by training low-rank matrices.

## Technical Significance
The main_grad bug fix ensures proper gradient computation for LoRA fine-tuning on Ascend hardware. This is critical for correct weight updates during parameter-efficient adaptation of large models.

## Related
- LoRA (Low-Rank Adaptation)
- gradient computation