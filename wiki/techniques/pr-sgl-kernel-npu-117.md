---
id: technique-pr-sgl-kernel-npu-117
title: "PR Insight: sgl-project/sgl-kernel-npu #117"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - hccs
  - hccl-optimization
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/117"
---

# PR Insight: sgl-project/sgl-kernel-npu #117

**Title:** Fix the severe performance degradation issue of the top9 dispatch in normal mode compared to top8.

## Overview
This PR fixes a severe performance degradation where top9 dispatch in normal mode performed 3.6x worse than top8 (24.28 GB/s vs 87.82 GB/s over HCCS). The fix restores expected communication bandwidth.

## Technical Significance
The 3.6x performance degradation indicates a critical bug in top9 dispatch logic, likely related to padding, communication patterns, or tiling. The fix is essential for models requiring >8 experts and demonstrates the importance of proper expert count handling in MoE communication pipelines.

## Related
- `technique-hccl-optimization`, `hw-hccs`, `technique-moe`