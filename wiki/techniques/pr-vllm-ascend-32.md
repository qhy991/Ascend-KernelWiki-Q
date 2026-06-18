---
id: technique-pr-vllm-ascend-32
title: "PR Insight: vllm-project/vllm-ascend #32"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - rope
  - performance
  - data-reuse
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/32"
---

# PR Insight: vllm-project/vllm-ascend #32

**Title:** [Rope][Platform] optimize the to conversion in rope forward and reset default block_size in platform.py

## Overview
This PR optimizes rope forward by eliminating redundant dtype/device conversions, and increases the default block_size from 16 to 128 in platform.py. Ascend devices have better memory affinity with 128-block alignment, improving cache efficiency.

## Technical Significance
Two performance optimizations: (1) avoiding unnecessary tensor conversions in rope reduces overhead in the hot attention path, and (2) larger block_size improves memory alignment for Ascend's memory hierarchy, reducing bank conflicts and improving bandwidth utilization.

## Related
- technique-rope
- technique-bank-conflict-avoidance