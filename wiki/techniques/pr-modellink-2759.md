---
id: technique-pr-modellink-2759
title: "PR Insight: Ascend/ModelLink #2759"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - qwen3
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2759"
---

# PR Insight: Ascend/ModelLink #2759

**Title:** add qwen3 235b scripts and update 0day scripts

## Overview
This PR adds training and evaluation scripts for the Qwen3 235B model, a very large-scale language model. It also updates existing 0day scripts to ensure compatibility and optimal performance across the model family.

## Technical Significance
Qwen3 235B represents the upper end of current model sizes, requiring distributed training across multiple Ascend NPUs. The scripts include necessary configurations for tensor parallelism, pipeline parallelism, and data parallelism to enable training at this scale.

## Related
- technique-hccl-optimization