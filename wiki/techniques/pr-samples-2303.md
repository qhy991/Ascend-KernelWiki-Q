---
id: technique-pr-samples-2303
title: "PR Insight: Ascend/samples #2303"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - ascendc
  - api-migration
  - infinity
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2303"
---

# PR Insight: Ascend/samples #2303

**Title:** 【24】算子样例去除Ascend C命名空间，更改API使用方式——infinity

## Overview
This PR refactors operator samples by removing the Ascend C namespace and updating API usage patterns for the Infinity operator. This is part of modernizing the samples to align with current AscendC API conventions.

## Technical Significance
Demonstrates the transition from legacy Ascend C API patterns to modern API usage without explicit namespace dependencies. This migration pattern is important for maintaining compatibility with current AscendC development practices.

## Related
- `technique-format-conversion`
- `wiki-language-ascendc`