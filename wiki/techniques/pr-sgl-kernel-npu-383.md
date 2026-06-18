---
id: technique-pr-sgl-kernel-npu-383
title: "PR Insight: sgl-project/sgl-kernel-npu #383"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - layout-kernel
  - bugfix
  - expert-scaling
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/383"
---

# PR Insight: sgl-project/sgl-kernel-npu #383

**Title:** Fix the bug that the layout kernel crashed when the num of experts is no less than 384

## Overview
This PR fixes a crash in the DeepEP layout kernel that occurred when the number of experts exceeded 383. The modification also disables layout output verification in internode tests to reduce test duration, since correctness can be verified through dispatch-combine result testing. Performance testing shows stable operation with 256, 384, and 512 experts.

## Technical Significance
Fixing the layout kernel crash enables DeepEP to support very large-scale MoE models with hundreds of experts, which is essential for state-of-the-art models using extensive expert parallelism. The optimization of test procedures maintains verification quality while reducing CI execution time.

## Related
- `kernel-dispatch-layout`, `kernel-moe-layout`, `technique-expert-scaling`, `technique-bugfix`