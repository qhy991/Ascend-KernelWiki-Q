---
id: technique-pr-samples-2631
title: "PR Insight: Ascend/samples #2631"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - jpeg
  - vpc
  - alignment
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2631"
---

# PR Insight: Ascend/samples #2631

**Title:** JPG图片解码之后，返回图片宽/高应该为对齐之后的宽高

## Overview
This PR fixes the width/height values returned after JPG image decoding. The change ensures the reported dimensions reflect the aligned size after processing, not the original dimensions, which is important for downstream processing.

## Technical Significance
Proper image dimension handling is critical for image processing pipelines. Alignment is often required for NPU processing, and reporting aligned dimensions ensures correct memory allocation and processing in subsequent operations.

## Related
- `technique-format-conversion`
- `hw-vector-unit`