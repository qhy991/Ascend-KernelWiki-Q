---
id: technique-pr-mindspeed-1576
title: "PR Insight: Ascend/MindSpeed #1576"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - feature
  - gmm
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1576"
---

# PR Insight: Ascend/MindSpeed #1576

**Title:** flops计算新增支持gmm_add以及gmm接口

## Overview
This PR extends FLOPS (floating point operations) calculation to support GMM_ADD and GMM interfaces. This enables accurate performance profiling and benchmarking for models using GMM operations.

## Technical Significance
Improves profiling capabilities by accurately accounting for computational cost of GMM operations. Accurate FLOPS calculation is essential for performance analysis, optimization, and comparison across different model configurations.

## Related
- `kernel-gmm`
- `pattern-profiling`