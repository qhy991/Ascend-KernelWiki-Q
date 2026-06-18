---
id: technique-pr-sgl-kernel-npu-54
title: "PR Insight: sgl-project/sgl-kernel-npu #54"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - combine
  - memory-management
  - bugfix
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu #54"
---

# PR Insight: sgl-project/sgl-kernel-npu #54

**Title:** fix combine memory problem

## Overview
This PR fixes memory issues in the combine operation by scaling the global buffer size for normal dispatch and combine operations. Updates deep_ep.cpp buffer allocation logic and CI workflow.

## Technical Significance
Resolves memory allocation failures in Deep EP combine operations that could cause out-of-memory errors during MoE inference. Proper buffer sizing is critical for handling variable-sized expert outputs and preventing memory exhaustion during combine stages.

## Related
- technique-memory-management
- technique-moe-combine
- technique-buffer-optimization