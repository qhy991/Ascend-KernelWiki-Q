---
id: technique-pr-modellink-2387
title: "PR Insight: Ascend/ModelLink #2387"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - deepseek3
  - bugfix
  - weight-conversion
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2387"
---

# PR Insight: Ascend/ModelLink #2387

**Title:** fix bug of mtp when mcore2hf of deepseek3

## Overview
This PR fixes a bug in the MTP (Multi-Head Latent Attention Processing) module during the MCore-to-HuggingFace weight conversion for DeepSeekV3. The issue occurs when converting trained weights from ModelLink's internal format to the standard HuggingFace format.

## Technical Significance
Correct weight conversion is essential for model portability and deployment. DeepSeekV3's MLA structure uses compressed key-value representations that require precise transformation during format conversion. This bug fix ensures that the MTP component's weights are correctly mapped, preventing accuracy degradation when models are deployed in inference frameworks or transferred between training systems.

## Related
- `kernel-attention-mla`
- `technique-weight-conversion`