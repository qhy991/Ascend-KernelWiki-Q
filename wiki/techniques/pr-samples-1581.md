---
id: technique-pr-samples-1581
title: "PR Insight: Ascend/samples #1581"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - custom-operator
  - add-block
  - tbe
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1581"
---

# PR Insight: Ascend/samples #1581

**Title:** 增加AddBlockCust运行样例

## Overview
This PR adds a runtime sample for a custom AddBlock operator, demonstrating how to implement and invoke custom operators on Ascend NPUs.

## Technical Significance
Custom operator development is a key capability for implementing specialized operations not available in the standard operator library. The AddBlock sample likely shows TBE (Tensor Boost Engine) or AscendC operator implementation, build integration, and runtime invocation patterns that developers can adapt for their own custom kernels.

## Related
- `technique-custom-operator`
- `technique-tbe-dsl`
- `technique-ascendc`
- `kernel-elementwise`