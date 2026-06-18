---
id: technique-pr-samples-743
title: "PR Insight: Ascend/samples #743"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - environment-variables
  - typo
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/743"
---

# PR Insight: Ascend/samples #743

**Title:** 环境变量名称ASCEND_TENSOR_COMPLIER_INCLUDE拼写修改

## Overview
This PR fixes a typo in the environment variable name from "ASCEND_TENSOR_COMPLIER_INCLUDE" to "ASCEND_TENSOR_COMPILER_INCLUDE", correcting the spelling of "COMPILER" (was "COMPLIER").

## Technical Significance
Correcting environment variable names is important for ensuring that build and runtime systems can properly locate compiler include directories. Typos in environment variables can cause build failures or incorrect include path resolution.

## Related
- N/A (environment fix)