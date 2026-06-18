---
id: technique-pr-mindspeed-1588
title: "PR Insight: Ascend/MindSpeed #1588"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - feature
  - mc2
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1588"
---

# PR Insight: Ascend/MindSpeed #1588

**Title:** 支持MC2+MatMul Add特性

## Overview
This PR adds support for the MC2 (Matrix Core 2) combined with MatMul Add operation feature. This likely leverages hardware capabilities to fuse matrix multiplication with addition operations for improved performance.

## Technical Significance
Enables hardware-accelerated MatMul-Add fusion, reducing memory bandwidth usage and improving computational efficiency. This optimization is particularly beneficial for operations like bias addition in linear layers and attention mechanisms.

## Related
- `kernel-matmul`
- `technique-operator-fusion`