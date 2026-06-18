---
id: technique-pr-modellink-2555
title: "PR Insight: Ascend/ModelLink #2555"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - mamba
  - training
  - architecture
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2555"
---

# PR Insight: Ascend/ModelLink #2555

**Title:** ​[mamba] supports state_space_duality implementations for both mamba2 and mamba2_hybrid architectures.​

## Overview
This PR adds support for state_space_duality implementations for both Mamba2 and Mamba2_hybrid architectures. The implementation enables these advanced state-space models to run on the ModelLink framework.

## Technical Significance
Mamba2 and Mamba2_hybrid are state-space model architectures that offer alternatives to Transformers with different efficiency characteristics. State_space_duality is a specific implementation technique that requires specialized operators and memory access patterns optimized for Ascend NPUs.

## Related
- `technique-attention`