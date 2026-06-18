---
id: technique-pr-sgl-kernel-npu-436
title: "PR Insight: sgl-project/sgl-kernel-npu #436"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - low-latency
  - batch-size
  - topk
  - bugfix
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/436"
---

# PR Insight: sgl-project/sgl-kernel-npu #436

**Title:** Fix low_latency dispatch&combine checks with bs condition

## Overview
This PR fixes validation checks in low-latency dispatch and combine operators by adding axisBS_ != 0 condition when topk=-1 masking is enabled. The modification ensures proper handling of edge cases where batch size might be zero in certain tensor parallelism configurations.

## Technical Significance
The batch size validation fix prevents crashes or incorrect behavior in low-latency MoE operations when handling dynamic batch scenarios or edge cases in tensor parallel execution. Proper validation ensures robust operation across various deployment configurations.

## Related
- `kernel-deepep-low-latency`, `kernel-deepep-dispatch`, `kernel-deepep-combine`, `technique-bugfix`