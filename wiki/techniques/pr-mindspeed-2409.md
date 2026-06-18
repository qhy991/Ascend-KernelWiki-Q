---
id: technique-pr-mindspeed-2409
title: "PR Insight: Ascend/MindSpeed #2409"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - alibi
  - refactoring
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2409"
---

# PR Insight: Ascend/MindSpeed #2409

**Title:** 【问题单】【master分支】alibi重构问题单解决

## Overview
This PR resolves issues from ALiBi (Attention with Linear Biases) refactoring on the master branch. The fix addresses problems introduced during the restructuring of ALiBi code.

## Technical Significance
Corrects bugs in the ALiBi implementation after refactoring, ensuring proper attention computation with linear biases. Proper ALiBi implementation is critical for training models that need to handle variable-length sequences without positional embeddings.

## Related
- `kernel-attention-ascendc`
- `technique-alibi`