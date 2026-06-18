---
id: code-ascend-samples-aclnn
title: "Ascend Samples \u2014 aclnn Single-Operator Invocation"
type: source-code
repo: Ascend/samples
path: operator/aclnn
url: https://gitee.com/ascend/samples/tree/master/operator/aclnn
source_category: upstream-code
architectures:
- ascend910
- ascend910b
- ascend310p
tags:
- samples
- aclnn
- cpp
- operator
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- global-memory
- cube-unit
- vector-unit
techniques:
- workspace-management
kernel_types:
- matmul
- softmax
- layernorm
- elementwise
languages:
- cpp
---

# Ascend Samples — aclnn Single-Operator Invocation

Official samples for calling aclnn operators from host C++ code. This path provides code evidence for the two-phase GetWorkspaceSize/execute pattern, explicit workspace allocation, tensor descriptor creation, and stream-based operator launch.

## Code Location

- Repository: `Ascend/samples`
- Path: `operator/aclnn`
- URL: https://gitee.com/ascend/samples/tree/master/operator/aclnn
