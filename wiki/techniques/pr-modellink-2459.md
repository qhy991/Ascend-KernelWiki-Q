---
id: technique-pr-modellink-2459
title: "PR Insight: Ascend/ModelLink #2459"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - training
  - llama
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2459"
---

# PR Insight: Ascend/ModelLink #2459

**Title:** 对齐llama32-1b的GPU精度

## Overview
This PR aligns the numerical precision of Llama 3.2-1B model training between GPU and NPU implementations, ensuring equivalent results across different hardware platforms.

## Technical Significance
Numerical precision alignment is critical for model reproducibility and accuracy, ensuring that models trained on Ascend NPUs produce identical outputs to those trained on GPUs, facilitating cross-platform validation and deployment.

## Related
- `technique-precision-alignment` / `technique-fp16` / `technique-mixed-precision`