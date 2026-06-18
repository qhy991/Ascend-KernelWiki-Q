---
id: technique-pr-modellink-2628
title: "PR Insight: Ascend/ModelLink #2628"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - qwen3
  - training
  - conversion
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2628"
---

# PR Insight: Ascend/ModelLink #2628

**Title:** support qwen3 mcore2hf 0.6b 1.7b 4b 14b

## Overview
This PR adds support for converting Qwen3 models (0.6B, 1.7B, 4B, and 14B parameter sizes) from the ModelLink internal format (mcore) to HuggingFace format. The conversion scripts enable model interchange between frameworks.

## Technical Significance
Model format conversion is critical for ecosystem interoperability. Supporting multiple Qwen3 sizes allows researchers to train on Ascend using ModelLink's optimized distributed training, then deploy or fine-tune using HuggingFace tools. The conversion must handle tensor layout differences and attention mask formats.

## Related
- `technique-format-conversion`