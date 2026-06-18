---
id: technique-pr-modellink-2651
title: "PR Insight: Ascend/ModelLink #2651"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qlora
  - bugfix
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2651"
---

# PR Insight: Ascend/ModelLink #2651

**Title:** fix bug of ckpt in q_lora_rank

## Overview
This PR fixes a bug related to checkpoint handling in QLoRA rank operations. The issue likely affected how QLoRA ranks are saved, loaded, or managed during training, potentially causing errors or incorrect behavior during fine-tuning on Ascend hardware.

## Technical Significance
Checkpoint reliability is critical for long-running training jobs. Fixing checkpoint bugs in QLoRA ensures that training progress can be reliably saved and restored, preventing data loss and enabling robust fine-tuning workflows on Ascend NPUs.

## Related