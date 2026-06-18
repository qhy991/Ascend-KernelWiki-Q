---
id: technique-pr-modellink-2352
title: "PR Insight: Ascend/ModelLink #2352"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - bugfix
  - distributed-training
  - configuration
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2352"
---

# PR Insight: Ascend/ModelLink #2352

**Title:** fix some GPUS_PER_NODE to NPUS_PER_NODE

## Overview
This PR fixes configuration parameters by changing `GPUS_PER_NODE` to `NPUS_PER_NODE` throughout the codebase. This aligns the configuration terminology with Ascend's NPU architecture rather than GPU-centric naming.

## Technical Significance
Correct device configuration is critical for distributed training on Ascend clusters. Using `NPUS_PER_NODE` instead of `GPUS_PER_NODE` ensures proper device allocation, tensor parallelism setup, and collective communication initialization. This fix prevents configuration mismatches that could cause incorrect process binding, memory allocation errors, or communication failures in ModelLink's distributed training framework.

## Related
- `technique-distributed-training`
- `technique-hccl-optimization`