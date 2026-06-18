---
id: technique-pr-samples-992
title: "PR Insight: Ascend/samples #992"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - detection
  - bugfix
  - configuration
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/992"
---

# PR Insight: Ascend/samples #992

**Title:** 修改垃圾分类中ckpt文件名称不正确的问题

## Overview
Fixes an incorrect checkpoint (ckpt) file name in the garbage classification sample, which would cause model loading failures.

## Technical Significance
Correct checkpoint file paths are essential for inference pipelines. This fix ensures the garbage classification sample can load the pre-trained model correctly.

## Related
- `technique-inference-optimization` / `technique-model-loading`
