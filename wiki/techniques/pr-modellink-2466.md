---
id: technique-pr-modellink-2466
title: "PR Insight: Ascend/ModelLink #2466"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - mindspore
  - compatibility
  - framework
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2466"
---

# PR Insight: Ascend/ModelLink #2466

**Title:** 【兼容性方案-适配支持mindspore框架】

## Overview
This PR adds compatibility support for the MindSpore framework alongside PyTorch. MindSpore is Huawei's deep learning framework, and this enables ModelLink to work with both frameworks.

## Technical Significance
Framework compatibility allows ModelLink to leverage both PyTorch and MindSpore ecosystems on Ascend hardware. This provides flexibility for users and access to framework-specific optimizations.

## Related
- MindSpore
- framework compatibility