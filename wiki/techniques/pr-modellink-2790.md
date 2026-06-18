---
id: technique-pr-modellink-2790
title: "PR Insight: Ascend/ModelLink #2790"
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
  - "https://gitee.com/ascend/ModelLink/pulls/2790"
---

# PR Insight: Ascend/ModelLink #2790

**Title:** update the baseline in st

## Overview
This PR updates performance baselines in single-turn (ST) prediction scenarios. It refreshes benchmark data for comparison.

## Technical Significance
Maintaining accurate performance baselines is essential for tracking optimizations on Ascend NPUs. This update ensures users have current reference points for evaluating training performance improvements.

## Related
- `technique-distributed-training`