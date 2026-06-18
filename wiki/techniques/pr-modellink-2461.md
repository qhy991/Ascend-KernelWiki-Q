---
id: technique-pr-modellink-2461
title: "PR Insight: Ascend/ModelLink #2461"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - rope
  - operator
  - deprecation
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2461"
---

# PR Insight: Ascend/ModelLink #2461

**Title:** update:弃用老rope算子默认使用新算子

## Overview
This PR deprecates the old RoPE (Rotary Position Embedding) operator and makes the new operator the default. RoPE is essential for handling positional information in transformer models.

## Technical Significance
Updating to the new RoPE operator provides better performance and compatibility on Ascend hardware. The new operator likely includes optimizations for NPU execution and improved numerical stability.

## Related
- RoPE (Rotary Position Embedding)
- operator upgrade