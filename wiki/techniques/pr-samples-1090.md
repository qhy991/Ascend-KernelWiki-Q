---
id: technique-pr-samples-1090
title: "PR Insight: Ascend/samples #1090"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - jpege
  - alignment
  - buffer-size
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1090"
---

# PR Insight: Ascend/samples #1090

**Title:** 【轻量级 PR】：jpege在创建通道设置buf_size时，新增图片宽高16对齐

## Overview
This PR adds 16-byte alignment for image width and height when setting buffer size (buf_size) during JPEGE (JPEG encoder) channel creation. The alignment ensures proper memory layout for encoded images.

## Technical Significance
16-byte alignment is a common requirement for hardware processing and memory access optimization. Aligning image dimensions ensures that encoded output meets hardware expectations, improves memory access efficiency, and prevents potential errors or performance degradation in the JPEG encoding pipeline on Ascend DVPP.

## Related
- JPEG encoder (JPEGE) implementation
- Memory alignment requirements
- Buffer size calculations
- DVPP image processing