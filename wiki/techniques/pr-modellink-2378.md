---
id: technique-pr-modellink-2378
title: "PR Insight: Ascend/ModelLink #2378"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - deepseek
  - weight-conversion
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2378"
---

# PR Insight: Ascend/ModelLink #2378

**Title:** deepseek3权重转换支持mla-mm-split

## Overview
This PR adds support for MLA (Multi-head Latent Attention) multi-modal split during DeepSeek3 weight conversion, enabling proper handling of cross-modal attention components.

## Technical Significance
Enables proper weight conversion for DeepSeek3 models that use MLA with multi-modal capabilities, ensuring that attention heads for different modalities are correctly separated and converted to target formats.

## Related
- `technique-mla` / `technique-weight-conversion` / `technique-deepseek`