---
id: technique-pr-samples-1882
title: "PR Insight: Ascend/samples #1882"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - add
  - elementwise
  - ascendc
  - custom-operator
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1882"
---

# PR Insight: Ascend/samples #1882

**Title:** 新增add自定义算子案例多种调用方式

## Overview
This PR adds a comprehensive Add custom operator sample demonstrating multiple invocation methods. The sample shows different ways to integrate and call an AscendC Add kernel, including direct AscendCL calls, framework integration patterns, and various deployment scenarios.

## Technical Significance
Understanding multiple integration patterns is essential for deploying custom operators across different use cases. This sample demonstrates the flexibility of AscendC kernel integration, showing how the same kernel can be invoked through different APIs and deployment models, providing a complete reference for element-wise operator development on Ascend910/910B.

## Related
- `kernel-elementwise`
- `technique-custom-operator`
- `pattern-multi-integration`