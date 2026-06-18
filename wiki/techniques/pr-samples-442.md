---
id: technique-pr-samples-442
title: "PR Insight: Ascend/samples #442"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - python
  - opencv
  - environment
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/442"
---

# PR Insight: Ascend/samples #442

**Title:** 删除源码编opencv时带的python-opencv，修改python样例运行为python3.6

## Overview
This PR removes the Python-OpenCV included when compiling OpenCV from source and modifies the Python sample execution to use Python 3.6, likely to fix environment compatibility issues.

## Technical Significance
Resolves dependency conflicts and environment issues by removing bundled Python-OpenCV and standardizing on Python 3.6 for sample execution, ensuring better compatibility with Ascend software stack requirements.

## Related
- `technique-inference` - inference patterns using OpenCV