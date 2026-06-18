---
id: technique-pr-mindspeed-1769
title: "PR Insight: Ascend/MindSpeed #1769"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - 2dtp
  - lcoc
  - operator-fusion
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1769"
---

# PR Insight: Ascend/MindSpeed #1769

**Title:** 2dtp支持lcoc融合算子

## Overview
This PR adds support for LCOC (likely Layer-Context-Output-Combined) fused operators in 2D tensor parallelism. The fusion combines multiple operations into a single optimized kernel.

## Technical Significance
Operator fusion reduces memory access and improves performance by combining sequential operations. Supporting LCOC fusion in 2D tensor parallelism enables more efficient execution of attention and related operations on Ascend NPUs.

## Related
- technique-operator-fusion
- tensor-parallel patterns
- lcoc-optimization