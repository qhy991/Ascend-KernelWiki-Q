---
id: technique-pr-mindspeed-2650
title: "PR Insight: Ascend/MindSpeed #2650"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - feature
  - verl
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2650"
---

# PR Insight: Ascend/MindSpeed #2650

**Title:** Add TE class and args modification to support verl

## Overview
This PR adds TE (Transformer Engine) class modifications and argument changes to support VERL (Verifiable Reinforcement Learning) integration. The updates enable VERL-specific training workflows within the MindSpeed framework.

## Technical Significance
VERL extends standard training with verification capabilities for reinforcement learning applications. Supporting VERL requires extending the Transformer Engine and configuration system to handle verification-specific operations and logging. This feature enables advanced RL training workflows with built-in correctness verification.

## Related