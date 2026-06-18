---
id: technique-pr-mindspeed-2373
title: "PR Insight: Ascend/MindSpeed #2373"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - a2a
  - bmm
  - communication
  - shape
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2373"
---

# PR Insight: Ascend/MindSpeed #2373

**Title:** fix a2a ag bmm shape not equal

## Overview
This PR fixes a shape mismatch issue in a2a (all-to-all) and ag (all-gather) operations with BMM (Batch Matrix Multiply). The error occurs when tensor shapes are not aligned for collective communication operations.

## Technical Significance
Resolves shape validation errors in collective communication operations that precede matrix multiplication. Proper shape handling is critical for correct data distribution and aggregation in distributed training.

## Related
- `kernel-matmul-ascendc`
- `technique-hccl-optimization`
- `hw-hccs`