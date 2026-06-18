---
id: technique-pr-catlass-185
title: "PR Insight: Ascend/catlass #185"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - catlass
  - matmul
  - padding
  - splitk
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/185"
---

# PR Insight: Ascend/catlass #185

**Title:** 22_padding_splitk_matmul

## Overview
This PR adds example 22 demonstrating matmul with padding and split-K strategies. It shows how to handle shape constraints and partition workloads for better cube unit utilization.

## Technical Significance
Padding ensures matrices meet alignment requirements for efficient cube unit operation. Split-K divides the K dimension across multiple compute units, enabling better parallelism for large matrix multiplications and improved utilization of Ascend hardware resources.

## Related
- `kernel-matmul-ascendc`
- `technique-nz-tiling`
- `technique-pipeline-scheduling`