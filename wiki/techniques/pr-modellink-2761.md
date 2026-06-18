---
id: technique-pr-modellink-2761
title: "PR Insight: Ascend/ModelLink #2761"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - qwen
  - performance
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2761"
---

# PR Insight: Ascend/ModelLink #2761

**Title:** Optimize qwen2.5 72b

## Overview
This PR introduces optimizations for the Qwen2.5 72B model. The optimizations target training efficiency, memory usage, or inference performance for this large-scale language model on Ascend hardware.

## Technical Significance
Optimizing large 72B parameter models is challenging due to memory and computational requirements. These optimizations enable efficient training and inference of Qwen2.5 72B on Ascend NPUs, potentially through techniques like operator fusion, memory optimization, or communication overlap.

## Related
- technique-operator-fusion
- technique-data-reuse