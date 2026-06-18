---
id: technique-pr-modellink-2354
title: "PR Insight: Ascend/ModelLink #2354"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - deepseek3
  - weight-conversion
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2354"
---

# PR Insight: Ascend/ModelLink #2354

**Title:** v3权重mg转hf修正postprocess权重保存逻辑

## Overview
This PR fixes the postprocess weight saving logic during DeepSeekV3 weight conversion from ModelLink format to HuggingFace format. The correction ensures proper weight handling after the main conversion process.

## Technical Significance
Postprocessing in weight conversion often includes normalization layer scaling, dtype conversion, and layout reorganization. Incorrect postprocessing can lead to numerical discrepancies or model incompatibility. This fix ensures that DeepSeekV3 weights are correctly saved after conversion, maintaining accuracy and compatibility with HuggingFace inference frameworks for deployment on Ascend and other platforms.

## Related
- `technique-weight-conversion`
- `technique-normalization`