---
id: technique-pr-mindspeed-1543
title: "PR Insight: Ascend/MindSpeed #1543"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - moe
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1543"
---

# PR Insight: Ascend/MindSpeed #1543

**Title:** [bugfix] fix expert parallel group

## Overview
This PR fixes a bug related to expert parallel group management in MoE (Mixture of Experts) training. The issue likely involves incorrect group initialization or communication patterns between expert parallel ranks.

## Technical Significance
Resolves critical issues in MoE distributed training, ensuring correct communication and data exchange between expert groups. Proper expert parallel group management is essential for correct MoE computation and load balancing.

## Related
- `kernel-moe`
- `technique-hccl-optimization`