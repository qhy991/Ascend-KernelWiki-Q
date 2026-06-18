---
id: technique-pr-modellink-2419
title: "PR Insight: Ascend/ModelLink #2419"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - training
  - grpo
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2419"
---

# PR Insight: Ascend/ModelLink #2419

**Title:** fix grpo

## Overview
This PR fixes issues related to GRPO (Group Relative Policy Optimization), a reinforcement learning algorithm used for training language models with preference data.

## Technical Significance
Correct implementation of GRPO is essential for RLHF and preference-based training; this fix ensures that reward-based training works correctly on Ascend hardware, improving model alignment capabilities.

## Related
- `technique-rlhf` / `technique-grpo` / `technique-preference-learning`