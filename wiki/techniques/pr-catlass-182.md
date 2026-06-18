---
id: technique-pr-catlass-182
title: "PR Insight: Ascend/catlass #182"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - catlass
  - matmul
  - optimized-matmul
  - format-conversion
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/182"
---

# PR Insight: Ascend/catlass #182

**Title:** 扩展optimized_matmul_tla 支持B矩阵 zN nZ 排布

## Overview
This PR extends optimized_matmul_tla to support both zN and nZ data layouts for the B matrix. It adds format flexibility for the right operand in optimized matrix multiplication.

## Technical Significance
Supporting multiple B matrix formats allows optimized_matmul to work efficiently with different upstream data layouts without expensive format conversions. This reduces preprocessing overhead and enables better integration with various tensor storage schemes.

## Related
- `kernel-matmul-ascendc`
- `technique-nz-tiling`
- `technique-format-conversion`