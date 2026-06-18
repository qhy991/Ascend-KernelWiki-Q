---
id: technique-pr-cann-ops-adv-280
title: "PR Insight: Ascend/cann-ops-adv #280"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - combine
  - moe
  - routing
  - fullmesh
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/280"
---

# PR Insight: Ascend/cann-ops-adv #280

**Title:** dispatch and combine add fullmesh algorithm

## Overview
This PR adds a fullmesh algorithm variant to the dispatch and combine operations used in MoE models. The fullmesh approach implements all-to-all communication patterns for token distribution and expert output combination across devices.

## Technical Significance
Fullmesh communication patterns are essential for distributed MoE training where experts are sharded across multiple devices. This implementation optimizes the all-to-all communication using HCCL, reducing latency and improving bandwidth utilization. The dispatch phase sends tokens to expert shards, while the combine phase gathers expert outputs back. Adding fullmesh algorithm support provides flexibility for different network topologies and model parallelism strategies, enabling optimal performance for various cluster configurations.

## Related
- `technique-moe-ascendc`
- `technique-hccl-optimization`
- `technique-expert-parallelism`
- `technique-communication-patterns`