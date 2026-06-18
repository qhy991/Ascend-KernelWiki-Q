---
id: technique-pr-vllm-ascend-1381
title: "PR Insight: vllm-project/vllm-ascend #1381"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - qwen3-moe
  - aclgraph
  - moe
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1381"
---

# PR Insight: vllm-project/vllm-ascend #1381

**Title:** [Bugfix] Support Qwen3-MOE on aclgraph mode

## Overview
This PR fixes aclgraph mode support for Qwen3-MoE models, ensuring correct MoE operator execution in graph-optimized inference.

## Technical Significance
Enables aclgraph mode acceleration for Qwen3-MoE models, which previously failed due to incorrect operator handling. The fix updates fused MoE operators to work correctly within aclgraph's graph compilation and execution framework, providing performance benefits for MoE inference.

## Related
- `kernel-moe`
- `technique-aclgraph`
- `kernel-qwen3`