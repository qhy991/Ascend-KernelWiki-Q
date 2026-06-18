---
id: technique-pr-vllm-ascend-3533
title: "PR Insight: vllm-project/vllm-ascend #3533"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - nz-format
  - hccl-optimization
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3533"
---

# PR Insight: vllm-project/vllm-ascend #3533

**Title:** fix vl float model not support NZ format weight error

## Overview
fix vl float model not support nz mm op

## Technical Significance
Fixes VL float model NZ format weight support to ensure correct behavior with non-quantized models.

## Related
- `technique-nz-tiling`
