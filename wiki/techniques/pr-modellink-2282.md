---
id: technique-pr-modellink-2282
title: "PR Insight: Ascend/ModelLink #2282"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - moe
  - communication
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2282"
---

# PR Insight: Ascend/ModelLink #2282

**Title:** feat:支持moe-allgather-overlap-comm特性

## Overview
This PR adds support for MoE allgather overlap communication, a performance optimization technique that overlaps communication with computation for MoE expert routing.

## Technical Significance
Overlapping allgather communication with computation reduces communication overhead in MoE models, improving training throughput and scalability on distributed Ascend clusters. This is critical for large-scale MoE training.

## Related
- `technique-moe` / `technique-communication-overlap` / `technique-allgather` / `technique-hccl-optimization`