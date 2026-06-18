---
id: technique-pr-samples-1825
title: "PR Insight: Ascend/samples #1825"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - proto
  - operator
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1825"
---

# PR Insight: Ascend/samples #1825

**Title:** 回退op proto的路径

## Overview
This PR reverts the path for operator proto files, which define operator interfaces and attributes in the Ascend operator registry.

## Technical Significance
Correct operator proto file paths are essential for the operator registration and model compilation process. Proto files define operator schemas that the Ascend compiler uses for graph optimization and kernel selection, so maintaining accurate paths ensures proper model conversion and execution.

## Related
- `wiki-technique-operator-registration`