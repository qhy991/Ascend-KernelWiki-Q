---
id: technique-pr-samples-1265
title: "PR Insight: Ascend/samples #1265"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - cv
  - object-detection
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1265"
---

# PR Insight: Ascend/samples #1265

**Title:** 修改samples/ cplusplus / level3_application / 1_cv / detect_and_classify

## Overview
This PR modifies the detect_and_classify sample application in the CV (Computer Vision) category, which combines object detection and classification functionality.

## Technical Significance
The detect_and_classify application represents a multi-stage CV pipeline involving detection and classification operators. On Ascend hardware, such pipelines benefit from operator fusion techniques to reduce memory movement between stages, and efficient scheduling to overlap computation with data transfers between unified buffer and global memory.

## Related
- technique-operator-fusion
- technique-pipeline-scheduling
- wiki-hardware-unified-buffer