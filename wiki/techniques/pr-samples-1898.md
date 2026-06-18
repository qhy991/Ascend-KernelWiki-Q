---
id: technique-pr-samples-1898
title: "PR Insight: Ascend/samples #1898"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - add
  - elementwise
  - ascendc
  - cann
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1898"
---

# PR Insight: Ascend/samples #1898

**Title:** 修改add样例类型及shape，并适配最新社区CANN包

## Overview
This PR modifies the Add sample by changing the operator type and tensor shapes, and adapts the code to work with the latest community CANN package. The updates ensure the sample reflects current best practices and demonstrates AscendC implementation patterns compatible with the newest CANN release.

## Technical Significance
Tensor shapes and operator types significantly affect performance characteristics on Ascend hardware due to tiling strategies and memory hierarchy. The shape modifications demonstrate how to optimize for Ascend910/910B's compute and memory characteristics, while CANN compatibility updates show how to migrate between software versions.

## Related
- `kernel-elementwise`
- `technique-tiling`
- `pattern-cann-migration`