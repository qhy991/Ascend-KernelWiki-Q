---
id: technique-pr-mindspeed-2185
title: "PR Insight: Ascend/MindSpeed #2185"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - optimizer
  - feature
  - performance
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2185"
---

# PR Insight: Ascend/MindSpeed #2185

**Title:** feat: add virtual optimizer

## Overview
This PR adds virtual optimizer support to MindSpeed. Virtual optimizer is a technique for reducing optimizer state memory footprint without sacrificing convergence quality.

## Technical Significance
Virtual optimizer is a critical memory optimization for training large models on Ascend NPUs with limited unified buffer capacity. The technique reduces memory usage by sharing optimizer states (momentum and variance) across parameters or using reduced precision for these states. This optimization enables training of larger models or larger batch sizes within the same memory constraints. The feature is particularly important for distributed training where optimizer state memory can dominate total memory usage, especially for models with billions of parameters.

## Related
- `technique-nz-tiling`
- `technique-data-reuse`