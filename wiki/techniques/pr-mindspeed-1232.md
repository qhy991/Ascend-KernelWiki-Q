---
id: technique-pr-mindspeed-1232
title: "PR Insight: Ascend/MindSpeed #1232"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - moe
  - token-permute
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1232"
---

# PR Insight: Ascend/MindSpeed #1232

**Title:** fix: npu_moe_token_permute patch

## Overview
This PR fixes the NPU MoE (Mixture of Experts) token permutation implementation. Token permutation is essential for MoE models to route tokens to the appropriate expert models efficiently.

## Technical Significance
Correct token permutation is critical for MoE model performance and accuracy on Ascend NPUs. This fix ensures tokens are routed to experts efficiently, enabling MoE models to leverage Ascend's compute capabilities effectively while maintaining correct model behavior.

## Related
- kernel-moe
- technique-data-reuse