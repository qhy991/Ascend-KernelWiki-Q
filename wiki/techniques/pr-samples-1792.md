---
id: technique-pr-samples-1792
title: "PR Insight: Ascend/samples #1792"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - dvpp
  - jpegd
  - vpc
  - samples
  - compatibility
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1792"
---

# PR Insight: Ascend/samples #1792

**Title:** dvpp jpegd vpc功能适配不同处理器宽高对齐约束

## Overview
This PR adapts DVPP JPEG decoding and VPC (Vision Processing Center) functionality to handle width/height alignment constraints across different Ascend processor variants.

## Technical Significance
Different Ascend processors have varying memory alignment requirements for image operations. Adapting JPEG decoding and VPC samples ensures correct behavior across processor variants, preventing crashes or incorrect output due to misaligned memory accesses.

## Related
- `hw-dvpp`
- `wiki-technique-image-preprocessing`