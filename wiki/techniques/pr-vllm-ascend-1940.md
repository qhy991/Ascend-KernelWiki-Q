---
id: technique-pr-vllm-ascend-1940
title: "PR Insight: vllm-project/vllm-ascend #1940"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3-moe
  - aclgraph
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1940"
---

# PR Insight: vllm-project/vllm-ascend #1940

**Title:** [0.9.1][Bugfix]Support Qwen3-MOE on aclgraph mode in no dp case

## Overview
This PR fixes the fused_moe.py file to support Qwen3-MoE models on aclgraph mode when data parallelism is not enabled. The fix enables proper Qwen3-MoE execution in aclgraph mode.

## Technical Significance
Bugfix for Qwen3-MoE aclgraph support. Aclgraph mode provides better performance through graph execution, and supporting Qwen3-MoE in this mode is essential for production deployment.

## Related
- `kernel-moe-ascendc`
- `technique-aclgraph`
- `technique-qwen3-moe`