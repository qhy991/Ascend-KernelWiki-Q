---
id: technique-pr-catlass-232
title: "PR Insight: Ascend/catlass #232"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - catlass
  - auto-tuning
  - shared-library
  - kernel-launch
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/232"
---

# PR Insight: Ascend/catlass #232

**Title:** [mstuner_catlass] P2 - add libcatlass_kernels.so and provide universal kernel launch API to mstuner

## Overview
This PR adds a shared library (libcatlass_kernels.so) and provides a universal kernel launch API for the mstuner auto-tuning framework. It enables efficient kernel exploration and benchmarking.

## Technical Significance
A universal kernel launch API simplifies auto-tuner integration by providing a consistent interface for testing different kernel variants. The shared library enables runtime loading of optimized kernels without recompilation, which is essential for efficient search space exploration.

## Related
- `kernel-matmul-ascendc`
- `technique-pipeline-scheduling`