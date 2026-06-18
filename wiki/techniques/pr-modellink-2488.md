---
id: technique-pr-modellink-2488
title: "PR Insight: Ascend/ModelLink #2488"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - evaluation
  - environment
  - documentation
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2488"
---

# PR Insight: Ascend/ModelLink #2488

**Title:** 修复eval使用source环境变量sh，另外修复部分文档中未标注环境变量source

## Overview
This PR fixes evaluation scripts to properly source environment variables and updates documentation to indicate required environment variable sourcing. This ensures correct environment setup for running evaluations.

## Technical Significance
Proper environment variable handling ensures correct library paths and configurations for running evaluations on Ascend hardware. Documentation updates prevent user errors.

## Related
- environment setup
- evaluation scripts