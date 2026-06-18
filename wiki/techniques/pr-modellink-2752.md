---
id: technique-pr-modellink-2752
title: "PR Insight: Ascend/ModelLink #2752"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - bugfix
  - mamba
  - checkpoint
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2752"
---

# PR Insight: Ascend/ModelLink #2752

**Title:** fix ckpt of mamba2

## Overview
This PR fixes a checkpoint handling issue for the Mamba2 model. The fix resolves errors when saving or loading Mamba2 model checkpoints during training or inference workflows.

## Technical Significance
Correct checkpoint handling is essential for training large models like Mamba2. This fix ensures that training state can be reliably saved and restored on Ascend NPUs, enabling long training runs and model resumption without corruption.

## Related
- technique-operator-fusion