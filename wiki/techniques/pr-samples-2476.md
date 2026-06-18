---
id: technique-pr-samples-2476
title: "PR Insight: Ascend/samples #2476"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - matmul
  - quantization
  - tiling
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2476"
---

# PR Insight: Ascend/samples #2476

**Title:** 修改QuantMatMulCustom算子tiling问题

## Overview
This PR fixes tiling issues in the QuantMatMulCustom operator (from PR #2462). Tiling determines how large matrices are broken down for processing by the cube unit and is critical for performance and correctness.

## Technical Significance
Tiling bugs can cause incorrect results or performance degradation. Fixing these issues demonstrates proper tiling strategies for quantized matmul, which must account for quantization-specific alignment and padding requirements.

## Related
- `kernel-matmul-ascendc`, `technique-quantization`, `technique-nz-tiling`