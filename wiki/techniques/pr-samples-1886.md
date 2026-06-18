---
id: technique-pr-samples-1886
title: "PR Insight: Ascend/samples #1886"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - tensorflow
  - ascendc
  - add
  - custom-operator
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1886"
---

# PR Insight: Ascend/samples #1886

**Title:** 添加TensorFlow调用Ascend C AddCustom算子样例

## Overview
This PR adds a sample demonstrating how to invoke the AscendC AddCustom operator from TensorFlow. The sample shows the integration pattern for binding custom AscendC kernels as TensorFlow operators, enabling TensorFlow models to leverage high-performance NPU kernels while maintaining framework-level convenience.

## Technical Significance
TensorFlow integration is essential for bringing existing TensorFlow models to Ascend NPUs. This sample provides reference code for the TensorFlow/AscendC boundary, demonstrating how to pass tensors between TensorFlow and AscendC kernels, handle data conversions, and manage memory across the interface on Ascend910/910B.

## Related
- `technique-custom-operator`
- `pattern-tensorflow-interop`
- `kernel-elementwise`