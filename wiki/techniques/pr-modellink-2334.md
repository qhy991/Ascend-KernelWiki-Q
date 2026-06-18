---
id: technique-pr-modellink-2334
title: "PR Insight: Ascend/ModelLink #2334"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - qwen2moe
  - optimization
  - performance
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2334"
---

# PR Insight: Ascend/ModelLink #2334

**Title:** update qwen2moe update for faster

## Overview
This PR updates Qwen2-MoE implementation for faster training and inference. The optimizations improve performance of MoE operations on Ascend hardware.

## Technical Significance
MoE performance bottlenecks typically include expert selection all-to-all communication, expert kernel execution, and load balancing overhead. The update likely optimizes communication overlap with computation, improves expert kernel efficiency using Ascend's cube-unit, or implements better load balancing strategies. These improvements increase throughput for Qwen2-MoE training and inference on Ascend NPUs.

## Related
- `technique-moe-training`
- `technique-alltoall`
- `technique-cube-vector-overlap`
- `kernel-matmul`