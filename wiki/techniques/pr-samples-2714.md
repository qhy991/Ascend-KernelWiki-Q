---
id: technique-pr-samples-2714
title: "PR Insight: Ascend/samples #2714"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - python
  - inference
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2714"
---

# PR Insight: Ascend/samples #2714

**Title:** 修复python/resnet50异步推理示例的变量名拼写错误

## Overview
This PR fixes a variable name typo in the Python ResNet50 asynchronous inference sample. The correction improves code quality and ensures the sample demonstrates proper variable naming conventions for asynchronous inference workflows on Ascend hardware.

## Technical Significance
Ensures code correctness in async inference samples, which is critical for developers learning to implement asynchronous workflows with Ascend NPUs. Variable naming consistency helps prevent confusion when studying async inference patterns.

## Related
- `technique-operator-fusion`
- `technique-pipeline-scheduling`