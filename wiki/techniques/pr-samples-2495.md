---
id: technique-pr-samples-2495
title: "PR Insight: Ascend/samples #2495"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - mc2
  - allgather
  - reduce-scatter
  - hccl
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2495"
---

# PR Insight: Ascend/samples #2495

**Title:** mc2 allgatherMM & MMreduceScatter

## Overview
This PR adds samples for allgather and reduce-scatter operations combined with matrix multiplication in the MC2 context. Allgather with MM and reduce-scatter with MM are critical patterns for distributed training and inference.

## Technical Significance
Communication-compute overlap is essential for distributed ML performance. These samples show how to implement allgather+MM and MM+reduce-scatter patterns efficiently on Ascend, minimizing communication overhead.

## Related
- `technique-hccl-optimization`, `kernel-matmul-ascendc`, `technique-cube-vector-overlap`