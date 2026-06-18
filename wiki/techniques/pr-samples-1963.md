---
id: technique-pr-samples-1963
title: "PR Insight: Ascend/samples #1963"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kernel-launch
  - compilation
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1963"
---

# PR Insight: Ascend/samples #1963

**Title:** 修改Kernel直调算子编译脚本

## Overview
This PR modifies the compilation script for direct kernel invocation samples, improving the build process and ensuring proper compilation flags and library linking for AscendC kernels.

## Technical Significance
Improves the developer experience for direct kernel programming by fixing build configurations, making it easier to compile and test custom kernels without going through the full operator registration pipeline.

## Related
- `technique-instruction-queue`
- `kernel-matmul-ascendc`