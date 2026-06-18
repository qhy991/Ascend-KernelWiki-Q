---
id: technique-pr-vllm-ascend-7188
title: "PR Insight: vllm-project/vllm-ascend #7188"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - eplb
  - expert-parallelism
  - load-balancing
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7188"
---

# PR Insight: vllm-project/vllm-ascend #7188

**Title:** Feature: Support Unified Placement for Shared & Router Experts

## Overview
This PR implements unified placement for shared and router experts in Mixture of Experts (MoE) architecture, extending TopK routing to TopK+1 routing. It enables the Expert Load Balancer (EPLB) to optimize cross-device load balancing by treating shared experts as special router experts and enabling parallel execution of co-deployed experts on the same device.

## Technical Significance
This optimization matters for Ascend MoE inference because it eliminates the previous sequential execution constraint between shared and router experts. By expanding the load balancing solution space to include unified placement strategies, it improves hardware utilization and reduces inter-device load imbalance. The approach modifies weight loading logic, extends routing algorithms, and integrates seamlessly with existing EPLB mechanisms while maintaining backward compatibility.

## Related
- technique-moe
- technique-hccl-optimization
- technique-eplb