---
id: technique-pr-samples-1221
title: "PR Insight: Ascend/samples #1221"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - matmul
  - custom-op
  - edge
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1221"
---

# PR Insight: Ascend/samples #1221

**Title:** matmul样例适配小海思芯片

## Overview
This PR adapts the matmul operator sample for the HiSilicon (小海思) chip variant, ensuring compatibility with the specific hardware features and constraints of this Ascend edge platform.

## Technical Significance
Extends matmul sample coverage to HiSilicon-based Ascend variants, enabling developers to deploy matrix multiplication kernels on edge devices with different hardware configurations.

## Related
- `kernel-matmul-ascendc`
- `technique-nz-tiling`