---
id: technique-pr-mindspeed-2672
title: "PR Insight: Ascend/MindSpeed #2672"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspore
  - bugfix
  - memory
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2672"
---

# PR Insight: Ascend/MindSpeed #2672

**Title:** [mindspore][bugfix][master] fix out of mem

## Overview
This PR fixes an out-of-memory issue in the MindSpore backend implementation. The changes address memory allocation or management problems that caused OOM errors during training, particularly for large models or batch sizes.

## Technical Significance
Memory management is critical for training large language models on Ascend devices. This fix resolves OOM issues that could prevent model training, enabling larger batch sizes or models to fit within device memory limits. It may involve optimizing memory reuse, reducing tensor copies, or improving checkpointing strategies.

## Related
- `technique-data-reuse`
- `technique-double-buffering`