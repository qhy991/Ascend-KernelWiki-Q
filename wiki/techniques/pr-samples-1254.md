---
id: technique-pr-samples-1254
title: "PR Insight: Ascend/samples #1254"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - yuv
  - memory-alignment
  - cv
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1254"
---

# PR Insight: Ascend/samples #1254

**Title:** 【轻量级 PR】：yuv422格式高2对齐处理修改

## Overview
This PR modifies YUV422 format handling to correct height alignment to 2-pixel boundaries in the samples.

## Technical Significance
YUV422 format requires specific alignment constraints due to its chroma subsampling pattern (2:1 horizontal, no vertical subsampling). Height alignment to 2-pixel boundaries ensures efficient memory access patterns on Ascend's vector unit and prevents bank conflicts when processing YUV data in the unified buffer.

## Related
- wiki-hardware-bank-conflict-avoidance
- wiki-hardware-vector-unit
- technique-format-conversion