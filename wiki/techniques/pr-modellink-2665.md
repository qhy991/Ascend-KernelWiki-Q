---
id: technique-pr-modellink-2665
title: "PR Insight: Ascend/ModelLink #2665"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mamba
  - feature
  - training
  - performance
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2665"
---

# PR Insight: Ascend/ModelLink #2665

**Title:** [mamba] supports mamba2_2.7b pipeline, mamba2_8b st and optimizing mamba2 performance.

## Overview
This PR adds support for Mamba2 models with pipeline parallelism for the 2.7B parameter model and sequence parallelism for the 8B model. It also includes performance optimizations for Mamba2 training on Ascend hardware.

## Technical Significance
Mamba2 support with different parallelism strategies enables efficient training of state-space models on Ascend NPUs. Pipeline parallelism for larger models and sequence parallelism for efficient throughput, combined with performance optimizations, make Mamba2 training practical on Ascend platforms.

## Related
- technique-pipeline-scheduling
- technique-hccl-optimization