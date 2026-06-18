---
id: technique-pr-mindspeed-2449
title: "PR Insight: Ascend/MindSpeed #2449"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - allgather
  - overlap
  - communication
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2449"
---

# PR Insight: Ascend/MindSpeed #2449

**Title:** 【BUGFIX】修复mater allgather_overlap传参异常

## Overview
This PR fixes an exception in the allgather_overlap parameter passing in the master branch. Allgather is a collective communication operation that gathers data from all devices, and overlap improves performance by overlapping communication with computation.

## Technical Significance
Resolves parameter passing bugs in overlapped allgather operations, ensuring correct data aggregation across devices. Proper allgather overlap is critical for performance in distributed training scenarios.

## Related
- `technique-hccl-optimization`
- `technique-cube-vector-overlap`
- `hw-hccs`