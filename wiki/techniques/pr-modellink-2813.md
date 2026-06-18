---
id: technique-pr-modellink-2813
title: "PR Insight: Ascend/ModelLink #2813"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - performance
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2813"
---

# PR Insight: Ascend/ModelLink #2813

**Title:** [pytorch][sh] add time info baseline

## Overview
This PR adds time information baseline tracking to the PyTorch backend scripts. It enables performance monitoring and benchmarking of training runs on Ascend NPUs.

## Technical Significance
Performance tracking is essential for identifying bottlenecks and measuring optimization effectiveness. This baseline support helps users monitor and optimize training performance on Ascend NPUs, enabling data-driven performance improvements.

## Related
- `technique-distributed-training`