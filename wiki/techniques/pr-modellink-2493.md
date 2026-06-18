---
id: technique-pr-modellink-2493
title: "PR Insight: Ascend/ModelLink #2493"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - qwq
  - training
  - inference
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2493"
---

# PR Insight: Ascend/ModelLink #2493

**Title:** add QwQ-32B

## Overview
This PR adds support for the QwQ-32B model to ModelLink. QwQ is a language model family, and this adds training and inference infrastructure for the 32B parameter variant.

## Technical Significance
Adding QwQ-32B support expands ModelLink's model coverage for training on Ascend hardware. This includes memory optimizations, distributed training configuration, and inference support.

## Related
- QwQ model architecture
- model support