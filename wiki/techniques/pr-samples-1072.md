---
id: technique-pr-samples-1072
title: "PR Insight: Ascend/samples #1072"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - output-alignment
  - dvpp
  - configuration
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1072"
---

# PR Insight: Ascend/samples #1072

**Title:** sample中输出图片width stride不用最小32对齐

## Overview
This PR modifies sample code to remove the requirement for 32-byte alignment on output image width stride. Previously, output images enforced 32-byte alignment, but this restriction has been relaxed.

## Technical Significance
Relaxing alignment requirements provides more flexibility in image processing pipelines. While alignment can improve memory access efficiency, removing strict 32-byte constraints allows support for arbitrary image dimensions and simplifies buffer management. The change may reflect hardware improvements or updated DVPP capabilities.

## Related
- DVPP output alignment
- Stride configuration
- Image dimension flexibility
- Memory layout optimization