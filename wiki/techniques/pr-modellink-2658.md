---
id: technique-pr-modellink-2658
title: "PR Insight: Ascend/ModelLink #2658"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - training
  - recompute
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2658"
---

# PR Insight: Ascend/ModelLink #2658

**Title:** Fix recompute acc issue

## Overview
This PR fixes an accuracy issue related to activation recomputation in ModelLink. Activation recomputation is a memory optimization technique that trades computation for memory by recomputing activations during backward pass, and this fix addresses correctness issues in that implementation on Ascend hardware.

## Technical Significance
Activation recomputation is essential for training large models with limited memory. However, correctness is paramount. Fixing recompute accuracy issues ensures that users can benefit from memory savings without compromising model quality during training on Ascend NPUs.

## Related
- technique-data-reuse
- technique-unified-buffer