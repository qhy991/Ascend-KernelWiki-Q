---
id: technique-pr-vllm-ascend-1380
title: "PR Insight: vllm-project/vllm-ascend #1380"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - memory-leak
  - distributed
  - reduce-scatter
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1380"
---

# PR Insight: vllm-project/vllm-ascend #1380

**Title:** [Bugfix] Fix memory-leak caused by dist._functional_collectives.reduce_scatter_tensor

## Overview
This PR fixes a memory leak in the reduce-scatter tensor operation used during distributed inference.

## Technical Significance
Prevents unbounded memory growth during long-running inference by fixing resource cleanup in `reduce_scatter_tensor` operations. The memory leak was particularly problematic in MoE inference and other communication-heavy workloads. The fix updates communication operators and fused MoE to properly manage tensor lifecycle.

## Related
- `technique-hccl-optimization`
- `kernel-moe`
- `technique-distributed-inference`