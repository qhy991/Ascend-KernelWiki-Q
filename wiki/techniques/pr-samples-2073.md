---
id: technique-pr-samples-2073
title: "PR Insight: Ascend/samples #2073"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - samples
  - custom-op
  - reduce
  - norm
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2073"
---

# PR Insight: Ascend/samples #2073

**Title:** 新增LpNormV2CustomSample算子

## Overview
This PR adds a custom sample implementation of the LpNormV2 operator, which computes Lp norms across specified tensor dimensions. The sample demonstrates reduction operations in AscendC kernel development.

## Technical Significance
LpNorm involves reduction operations (sum, absolute value, power) that are compute-intensive on the Vector unit. The sample likely demonstrates efficient reduction strategies across tensor dimensions, possibly using intra-core and inter-core reduction patterns with proper synchronization.

## Related
- `technique-reduce`
- `technique-vector-unit`
- `technique-unified-buffer`