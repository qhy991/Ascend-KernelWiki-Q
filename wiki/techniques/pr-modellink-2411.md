---
id: technique-pr-modellink-2411
title: "PR Insight: Ascend/ModelLink #2411"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - training
  - padding
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2411"
---

# PR Insight: Ascend/ModelLink #2411

**Title:** Variable seq MTP no pad bugfix

## Overview
This PR fixes a bug related to padding in variable sequence length processing for MTP (likely Multi-Task Prediction or Model Training Pipeline), ensuring correct handling of variable-length sequences without unnecessary padding.

## Technical Significance
Proper handling of variable-length sequences without padding improves efficiency and correctness, especially for tasks with highly variable input lengths, reducing wasted computation on padding tokens.

## Related
- `technique-padding` / `technique-variable-sequence` / `technique-training`