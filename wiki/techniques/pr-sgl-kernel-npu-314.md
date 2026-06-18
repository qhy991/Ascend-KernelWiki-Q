---
id: technique-pr-sgl-kernel-npu-314
title: "PR Insight: sgl-project/sgl-kernel-npu #314"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - double-buffering
  - hccl-optimization
  - moe
  - pipeline-scheduling
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/314"
---

# PR Insight: sgl-project/sgl-kernel-npu #314

**Title:** Optimize the performance of the Combine Ant Moving function and the use of HCCL buffer

## Overview
This PR optimizes the DeepEP MoE "ant moving" (token migration between rounds) functionality by implementing double buffering to overlap communication with full-card synchronization. The optimization reduces the performance overhead from full-card synchronization in multi-round communication scenarios. Additionally, it reduces HCCL buffer usage for notify_dispatch from 408MB to 204MB, and removes unnecessary PipeBarrier calls.

## Technical Significance
The double-buffering technique significantly improves MoE performance for long sequence processing by hiding synchronization latency behind communication. Benchmarking shows framework-level TPS improvement from 1200 to 2106 on Qwen 235B prefill, demonstrating the impact of communication overlap optimization on end-to-end inference throughput.

## Related
- `technique-double-buffering`, `technique-hccl-optimization`, `kernel-moe-combine`, `hw-hccs`