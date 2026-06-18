---
id: technique-pr-sgl-kernel-npu-172
title: "PR Insight: sgl-project/sgl-kernel-npu #172"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - moe
  - combine
  - layered
  - optimization
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/172"
---

# PR Insight: sgl-project/sgl-kernel-npu #172

**Title:** optimize a2 layered combine kernel code

## Overview
Optimizes the A2 layered combine kernel code for DeepEP, providing two implementation versions: a two-server build (default) for lowest latency with exactly two servers, and a multi-server build for larger server counts at slightly higher latency cost.

## Technical Significance
The layered combine optimization provides flexible deployment options for A2 architecture, optimizing for either minimal latency (two-server scenario) or scalability (multi-server scenario). This flexibility allows users to choose the best implementation based on their deployment topology, improving overall DeepEP performance across different cluster configurations.

## Related
- `wiki-kernel-moe`
- `wiki-technique-hccl-optimization`
- `wiki-hardware-a2`
- `wiki-technique-layered`