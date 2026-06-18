---
id: technique-pr-samples-1273
title: "PR Insight: Ascend/samples #1273"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - cv
  - resize
  - padding
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1273"
---

# PR Insight: Ascend/samples #1273

**Title:** 【轻量级 PR】：单图多图抠图缩放边界填充资料修改

## Overview
This PR updates documentation and code for single-image and multi-image cropping, resizing, and boundary padding operations in the CV samples.

## Technical Significance
Image preprocessing operations like cropping, resizing, and padding are compute-intensive and memory-bound in CV pipelines. On Ascend hardware, these operations benefit from vector unit acceleration and careful memory alignment to avoid bank conflicts. Efficient padding operations are particularly important for maintaining alignment requirements when feeding data into subsequent operators.

## Related
- technique-vector-unit
- hw-bank-conflict-avoidance
- technique-pipeline-scheduling