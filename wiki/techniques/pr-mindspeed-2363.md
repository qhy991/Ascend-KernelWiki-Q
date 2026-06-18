---
id: technique-pr-mindspeed-2363
title: "PR Insight: Ascend/MindSpeed #2363"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - activation
  - probs
  - core-v0.12.1
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2363"
---

# PR Insight: Ascend/MindSpeed #2363

**Title:** fix: adaptation core_v0.12.1 which activation func without probs

## Overview
This PR fixes an adaptation issue in core version v0.12.1 for activation functions that don't use probabilities. Some activation functions don't require probability parameters, and this fix handles that case correctly.

## Technical Significance
Ensures activation functions work correctly when probability parameters are not required. Proper handling of different activation function signatures prevents errors in forward and backward passes.

## Related
- `kernel-elementwise-ascendc`
- `technique-activation-functions`