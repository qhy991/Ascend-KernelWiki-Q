---
id: technique-pr-vllm-ascend-2734
title: "PR Insight: vllm-project/vllm-ascend #2734"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - communication
  - optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2734"
---

# PR Insight: vllm-project/vllm-ascend #2734

**Title:** [Fix][MoE] Refine MoE communication strategy

## Overview
This PR refactors MoE communication method selection logic to optimize performance based on expert parallel configuration, SoC version (A2/A3), and token count. The adaptive strategy chooses between all-gather, all-to-all, and MC2 communication patterns for optimal throughput.

## Technical Significance
Adaptive communication strategy selection is crucial for MoE performance across different hardware generations and workload characteristics. The optimization ensures efficient utilization of Ascend NPU interconnect capabilities and reduces communication overhead in distributed MoE inference.

## Related
- `technique-moe`
- `technique-hccl-optimization`
- `kernel-fused-moe`
- `technique-communication`