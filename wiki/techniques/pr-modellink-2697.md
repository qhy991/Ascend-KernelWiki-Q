---
id: technique-pr-modellink-2697
title: "PR Insight: Ascend/ModelLink #2697"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspore
  - deepseek
  - documentation
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2697"
---

# PR Insight: Ascend/ModelLink #2697

**Title:** 【master】fix document and shell script for mindspore deepseek3

## Overview
This PR fixes documentation and shell script issues specifically for DeepSeekV3 model training with the MindSpore backend. It corrects errors in the training launch scripts and updates configuration documentation for DeepSeekV3 on Ascend.

## Technical Significance
DeepSeekV3 represents a significant advancement in MoE architecture. Accurate scripts and documentation are critical for successful deployment on Ascend hardware. This fix ensures users can reliably train DeepSeekV3 with MindSpore, supporting advanced MoE workflows on Ascend NPUs.

## Related
- technique-moe