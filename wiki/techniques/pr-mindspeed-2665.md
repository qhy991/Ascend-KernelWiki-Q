---
id: technique-pr-mindspeed-2665
title: "PR Insight: Ascend/MindSpeed #2665"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - lora
  - fine-tuning
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2665"
---

# PR Insight: Ascend/MindSpeed #2665

**Title:** fix lora target modules assertion bug

## Overview
This PR fixes an assertion error in the LoRA (Low-Rank Adaptation) target module selection logic. The bug caused failures when validating which model modules should receive LoRA adapters during parameter-efficient fine-tuning.

## Technical Significance
LoRA enables efficient fine-tuning by adding low-rank adapter matrices to specific model layers. Proper target module identification is critical for correct LoRA application. This fix ensures robust handling of module names and patterns, preventing runtime errors during LoRA fine-tuning workflows.

## Related