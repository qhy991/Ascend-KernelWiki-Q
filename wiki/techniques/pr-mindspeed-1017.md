---
id: technique-pr-mindspeed-1017
title: "PR Insight: Ascend/MindSpeed #1017"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - moe
  - mc2
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1017"
---

# PR Insight: Ascend/MindSpeed #1017

**Title:** Mc2 Moe Op Bug Fix

## Overview
This PR fixes bugs in Mc2 MoE (Mixture of Experts) operations. Mc2 likely refers to a specific MoE implementation variant or configuration in the MindSpeed framework.

## Technical Significance
Correct MoE operation is critical for MoE model accuracy and performance on Ascend NPUs. This bug fix ensures proper expert routing, load balancing, or computation in Mc2 MoE implementations, enabling reliable training and inference of MoE models.

## Related
- kernel-moe