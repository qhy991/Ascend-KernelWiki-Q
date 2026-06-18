---
id: technique-pr-samples-1681
title: "PR Insight: Ascend/samples #1681"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - tik2
  - custom-operator
  - demo
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1681"
---

# PR Insight: Ascend/samples #1681

**Title:** 新增tik2-demo custom_op样例工程

## Overview
This PR adds a new TIK2 custom operator demo sample project, demonstrating how to implement custom operators using the TIK2 (Tensor Inference Kernel) framework.

## Technical Significance
TIK2 is Ascend's intermediate representation for custom operator development. Custom operators enable developers to implement specialized computations not covered by the standard operator library. This sample provides a working example of TIK2 operator implementation, including the programming model and API usage.

## Related
- technique-custom-operator
- technique-tik2