---
id: technique-pr-mindspeed-1399
title: "PR Insight: Ascend/MindSpeed #1399"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - feature
  - tp-2d
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1399"
---

# PR Insight: Ascend/MindSpeed #1399

**Title:** tp-2d适配num_query_group+free优化（master)

## Overview
This PR adapts TP-2D (2D tensor parallelism) to support num_query_group parameter and includes free optimizations on the master branch. The changes likely involve query group handling and performance improvements.

## Technical Significance
Enhances TP-2D to work with grouped-query attention and includes performance optimizations. Support for num_query_group is essential for modern attention mechanisms like GQA (Grouped Query Attention) used in efficient transformer architectures.

## Related
- `kernel-attention`
- `technique-hccl-optimization`