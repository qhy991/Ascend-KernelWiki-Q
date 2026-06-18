---
id: technique-pr-samples-1433
title: "PR Insight: Ascend/samples #1433"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - onnx
  - non-uniform-quantization
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1433"
---

# PR Insight: Ascend/samples #1433

**Title:** 修复amct_onnx非均匀量化示例samples中不产生nuq配置

## Overview
This PR fixes an issue in the AMCT ONNX non-uniform quantization sample where the NUQ (Non-Uniform Quantization) configuration file was not being generated. The fix ensures the quantization workflow produces the expected configuration output.

## Technical Significance
Non-uniform quantization can achieve better accuracy than uniform quantization at similar bit-widths. Fixing the NUQ configuration generation is critical for developers to explore advanced quantization techniques for ONNX models on Ascend hardware.

## Related
- technique-quantization
- technique-non-uniform-quantization
- technique-model-compression