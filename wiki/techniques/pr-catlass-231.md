---
id: technique-pr-catlass-231
title: "PR Insight: Ascend/catlass #231"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - catlass
  - auto-tuning
  - search-space
  - kernel-generation
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/231"
---

# PR Insight: Ascend/catlass #231

**Title:** [mstuner_catlass] P1 - support kernel source generation from search space

## Overview
This PR adds support for generating kernel source code from search space definitions in the mstuner_catlass auto-tuning framework. It enables automated kernel exploration and optimization.

## Technical Significance
Search space-based kernel generation is essential for auto-tuning systems. It allows the tuner to explore different tiling strategies, pipeline configurations, and format choices automatically, finding optimal configurations for specific workload shapes on Ascend hardware.

## Related
- `kernel-matmul-ascendc`
- `technique-nz-tiling`
- `technique-pipeline-scheduling`