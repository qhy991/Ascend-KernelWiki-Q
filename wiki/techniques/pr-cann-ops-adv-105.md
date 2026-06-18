---
id: technique-pr-cann-ops-adv-105
title: "PR Insight: cann-ops-adv #105"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - flash-attention
  - attention
  - testing
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/105"
---

# PR Insight: cann-ops-adv #105 - modify FAG UT runkernel

## Overview
This PR modifies the unit test execution for FAG (FlashAttentionScoreGrad), specifically updating how the runkernel function is called or configured during testing.

## Technical Significance
Unit test improvements ensure better validation of attention gradient computation. The modification likely addresses test stability, improves coverage, or fixes issues with kernel execution in the test environment, ensuring correct gradient computation for attention backpropagation.

## Related
- `kernel-flash-attention`
- `kernel-attention`
- `technique-debugging`