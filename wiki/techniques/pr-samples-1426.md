---
id: technique-pr-samples-1426
title: "PR Insight: Ascend/samples #1426"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - samples
  - vpc
  - image-alignment
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1426"
---

# PR Insight: Ascend/samples #1426

**Title:** 修复关于在310P3上需手动2对齐vpc输入输出图片宽高的问题

## Overview
This PR fixes an issue on Ascend 310P3 where VPC (Vision Processing Center) input/output image widths and heights need manual 2-alignment. The fix likely adds automatic alignment or updates the sample to handle the alignment requirement transparently.

## Technical Significance
Hardware alignment requirements are common for memory efficiency. Understanding and handling these requirements is important for correct image processing on Ascend 310P, especially with VPC operations.

## Related
- hw-vpc
- technique-memory-alignment