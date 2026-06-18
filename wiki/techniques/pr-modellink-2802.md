---
id: technique-pr-modellink-2802
title: "PR Insight: Ascend/ModelLink #2802"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - bugfix
  - configuration
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2802"
---

# PR Insight: Ascend/ModelLink #2802

**Title:** delete not-found arg gradient_accumulation_fusion

## Overview
This PR removes a non-existent argument (gradient_accumulation_fusion) from the PyTorch backend configuration. It cleans up invalid parameter references.

## Technical Significance
Removing invalid arguments prevents configuration errors on Ascend NPUs. This cleanup ensures users don't encounter errors from deprecated or non-existent parameters, improving framework stability.

## Related
- `technique-distributed-training`