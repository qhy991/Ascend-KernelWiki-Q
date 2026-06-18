---
id: technique-pr-samples-2806
title: "PR Insight: Ascend/samples #2806"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - conv2d
  - matmul
  - include-path
  - build
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2806"
---

# PR Insight: Ascend/samples #2806

**Title:** conv2d matmul include path add arm and acl path

## Overview
This PR adds ARM and ACL (Ascend Computing Language) include paths to conv2d and matmul samples. This change likely improves cross-platform compatibility or ensures proper header file resolution during compilation.

## Technical Significance
Correct include paths are essential for successful compilation of AscendC kernels. Adding ARM and ACL paths ensures samples build correctly across different development environments and support various Ascend hardware platforms.

## Related
- kernel-matmul-ascendc
- technique-operator-fusion