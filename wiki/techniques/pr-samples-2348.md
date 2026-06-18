---
id: technique-pr-samples-2348
title: "PR Insight: Ascend/samples #2348"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - cube-group
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2348"
---

# PR Insight: Ascend/samples #2348

**Title:** 增加CubeGroupCustomSamples样例

## Overview
This PR adds new sample code for CubeGroupCustom samples to the Ascend samples repository. The CubeGroup functionality in AscendC allows developers to work with groups of cube units for more advanced parallelization strategies in kernel development.

## Technical Significance
CubeGroup samples help developers understand how to leverage multiple cube units in parallel, which is essential for achieving optimal performance on Ascend 910/910B hardware. This fills a documentation gap for advanced AscendC programming patterns.

## Related
- `hw-cube-unit`, `technique-operator-fusion`