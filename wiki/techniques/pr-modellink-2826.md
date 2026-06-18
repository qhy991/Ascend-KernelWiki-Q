---
id: technique-pr-modellink-2826
title: "PR Insight: Ascend/ModelLink #2826"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - deepseek
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2826"
---

# PR Insight: Ascend/ModelLink #2826

**Title:** [pytorch][sh]update mindspeed commit id for deepseek3

## Overview
This PR updates the MindSpeed commit ID used for DeepSeek-V3 training scripts in the PyTorch backend. It ensures compatibility with the latest MindSpeed optimizations.

## Technical Significance
Keeping training scripts synchronized with upstream MindSpeed improvements ensures access to the latest performance optimizations and bug fixes for DeepSeek-V3 training on Ascend NPUs, potentially improving training efficiency and stability.

## Related
- `technique-distributed-training`