---
id: technique-pr-samples-764
title: "PR Insight: Ascend/samples #764"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - onnx
  - quantization
  - fusion
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/764"
---

# PR Insight: Ascend/samples #764

**Title:** amct_onnx 训练后量化，添加融合信息文件。

## Overview
This PR adds fusion information files for post-training quantization using AMCT (Ascend Model Compression Toolkit) with ONNX models. The fusion information enables operator fusion optimizations during the quantization process.

## Technical Significance
Adding fusion information for AMCT ONNX quantization enables advanced optimization techniques that combine multiple operators into fused kernels, improving inference performance. This is critical for efficient model deployment on Ascend hardware with reduced memory footprint and faster execution.

## Related
- N/A (quantization optimization)