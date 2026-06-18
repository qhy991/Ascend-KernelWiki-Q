---
id: technique-pr-samples-2770
title: "PR Insight: Ascend/samples #2770"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - matmul
  - hccl-optimization
  - allgather
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2770"
---

# PR Insight: Ascend/samples #2770

**Title:** allgathermm optimize

## Overview
This PR optimizes the allgather matrix multiplication operation in samples. AllGatherMM is a communication-computation overlap pattern used in distributed matrix multiplication for large models.

## Technical Significance
AllGatherMM optimization is crucial for distributed training and inference of large models. Efficient allgather operations combined with matrix multiplication can significantly improve multi-device performance by overlapping communication and computation.

## Related
- `pattern-communication-computation-overlap`, `technique-hccl-optimization`, `technique-pipeline-scheduling`