---
id: technique-pr-modellink-2821
title: "PR Insight: Ascend/ModelLink #2821"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - oom
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2821"
---

# PR Insight: Ascend/ModelLink #2821

**Title:** [pytorch][bugfix]fix 405b-128k oom

## Overview
This PR fixes an out-of-memory (OOM) issue for 405B parameter models with 128K context length in the PyTorch backend. It addresses memory management for very large model training.

## Technical Significance
Training 405B models with 128K context requires extreme memory efficiency. This fix enables successful training of these large-scale models on Ascend NPUs by resolving memory allocation issues, pushing the boundaries of what's possible on the platform.

## Related
- `technique-attention`
- `technique-data-reuse`