---
id: technique-pr-mindspeed-2443
title: "PR Insight: Ascend/MindSpeed #2443"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - docs
  - alibi
  - documentation
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2443"
---

# PR Insight: Ascend/MindSpeed #2443

**Title:** docs: change alibi doc

## Overview
This PR changes documentation for the ALiBi (Attention with Linear Biases) feature. ALiBi is an attention mechanism that replaces positional embeddings with linear biases, enabling better extrapolation to longer sequences.

## Technical Significance
Updates documentation to reflect correct usage and behavior of ALiBi in MindSpeed. ALiBi is important for training models that handle variable-length sequences, and accurate documentation prevents misuse.

## Related
- `kernel-attention-ascendc`
- `technique-alibi`