---
id: technique-pr-samples-2740
title: "PR Insight: Ascend/samples #2740"
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
  - "https://gitee.com/ascend/samples/pulls/2740"
---

# PR Insight: Ascend/samples #2740

**Title:** allgathermm opt

## Overview
This PR optimizes the allgather matrix multiplication operation. The optimization improves performance for distributed matrix multiplication workloads.

## Technical Significance
AllGatherMM is a key pattern for large model training and inference. Optimizing this operation directly impacts multi-device performance for LLMs and other large models.

## Related
- `pattern-communication-computation-overlap`, `technique-hccl-optimization`, `technique-pipeline-scheduling`