---
id: technique-pr-modellink-2836
title: "PR Insight: Ascend/ModelLink #2836"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - qwen
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2836"
---

# PR Insight: Ascend/ModelLink #2836

**Title:** [pytorch][sh]update Qwen2.5 14b/72b 32K scripts

## Overview
This PR updates training scripts for Qwen2.5 14B and 72B models with 32K context length support. It ensures proper configuration for long-context training on Ascend NPUs.

## Technical Significance
Long-context training requires careful attention to memory management and attention mechanisms. These updates enable proper training of Qwen2.5 models with extended context on Ascend NPUs, supporting applications requiring longer input sequences.

## Related
- `technique-attention`
- `technique-distributed-training`