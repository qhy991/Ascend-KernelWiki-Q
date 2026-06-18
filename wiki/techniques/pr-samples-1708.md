---
id: technique-pr-samples-1708
title: "PR Insight: Ascend/samples #1708"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - crowd-counting
  - object-detection
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1708"
---

# PR Insight: Ascend/samples #1708

**Title:** 新增样例sampleCrowdCounting

## Overview
This PR adds a new crowd counting sample to the repository, demonstrating how to implement crowd density estimation on Ascend hardware for applications like public safety and retail analytics.

## Technical Significance
Crowd counting is a specialized computer vision task that often uses density map regression or detection-based approaches. This sample shows how to implement such models efficiently on Ascend NPUs, handling the computational requirements of density estimation.

## Related
- technique-density-estimation
- technique-object-detection