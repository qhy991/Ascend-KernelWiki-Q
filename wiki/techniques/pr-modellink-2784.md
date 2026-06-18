---
id: technique-pr-modellink-2784
title: "PR Insight: Ascend/ModelLink #2784"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - mindspore
  - matmul
  - optimization
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2784"
---

# PR Insight: Ascend/ModelLink #2784

**Title:** add npu_matmul_add_fp32 and npu_groupmatmul_add_fp32(mindspore patch)

## Overview
This PR adds FP32 matmul-add and grouped matmul-add NPU operators as MindSpore patches. It provides optimized fused operations for matrix multiplication with addition.

## Technical Significance
Fused matmul-add operations reduce memory bandwidth requirements and improve numerical stability with FP32 precision. These patches optimize matrix operations on Ascend NPUs, improving training efficiency and accuracy for models requiring higher precision computation.

## Related
- `technique-matmul`
- `technique-operator-fusion`