---
id: technique-pr-sgl-kernel-npu-508
title: "PR Insight: sgl-project/sgl-kernel-npu #508"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - deepep
  - hccl-optimization
  - communication
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/508"
---

# PR Insight: sgl-project/sgl-kernel-npu #508

**Title:** [NPU][Feat] Add alltoall mode on deepep

## Overview
This PR adds all-to-all communication mode support to the DeepEP framework for normal mode operation. The feature enables users to enable all-to-all functionality by setting the environment variable `DEEP_USE_ALLTOALL_MODE=1`. The implementation includes new all-to-all communication primitives and buffer management enhancements, with demonstrated performance improvements and maintained numerical accuracy.

## Technical Significance
Adding all-to-all mode to DeepEP provides an alternative communication strategy for expert routing in MoE inference. All-to-all communication can offer better performance characteristics for certain MoE configurations by reducing the number of communication steps or improving load balancing across devices. This enhancement gives users more flexibility in optimizing their MoE inference pipelines for specific workloads and hardware configurations.

## Related
- `technique-hccl-optimization`
- `pattern-expert-parallelism`
- `technique-moe-dispatch`
- `pattern-communication-strategy`