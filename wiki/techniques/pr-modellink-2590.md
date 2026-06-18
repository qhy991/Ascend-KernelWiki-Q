---
id: technique-pr-modellink-2590
title: "PR Insight: Ascend/ModelLink #2590"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - sft
  - attention
  - mask
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2590"
---

# PR Insight: Ascend/ModelLink #2590

**Title:** sft场景适配tnd模式fa算子mask

## Overview
This PR adapts the TND (time-number-dimension) mode FA (Flash Attention) operator mask for supervised fine-tuning (SFT) scenarios. The changes ensure correct attention masking behavior during fine-tuning workflows.

## Technical Significance
Correct attention masking is critical for fine-tuning, where specific positions must be masked or preserved based on the fine-tuning data format. Adapting the FA operator mask for TND mode ensures efficient attention computation while maintaining correct semantics on Ascend NPUs.

## Related
- `technique-flash-attention`