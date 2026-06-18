---
id: technique-pr-samples-1020
title: "PR Insight: Ascend/samples #1020"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - scatter
  - bugfix
  - api-compatibility
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1020"
---

# PR Insight: Ascend/samples #1020

**Title:** 修改scatter_nd_add引入未开放接口get_bit_len问题

## Overview
Fixes an issue in scatter_nd_add where an unreleased interface `get_bit_len` was being referenced, likely causing API compatibility problems.

## Technical Significance
Ensures samples only use publicly available and stable APIs, preventing runtime failures when run on different CANN versions. Scatter operations are important for sparse tensor manipulations in ML workloads.

## Related
- `technique-sparse-operations` / `technique-api-compatibility`
