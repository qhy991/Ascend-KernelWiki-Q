---
id: technique-pr-vllm-ascend-2946
title: "PR Insight: vllm-project/vllm-ascend #2946"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - aclgraph
  - multi-stream
  - pipeline-scheduling
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2946"
---

# PR Insight: vllm-project/vllm-ascend #2946

**Title:** [Feature] Support moe multi-stream for aclgraph.

## Overview
This PR implements multi-stream execution for MoE models in ACL Graph mode by computing shared experts in a separate stream that overlaps with routing experts. It modifies common_fused_moe.py, adds test cases, and updates configuration options.

## Technical Significance
The multi-stream approach enables pipeline parallelism between shared expert computation and routed expert computation, improving resource utilization on Ascend NPUs. By overlapping these computations, the PR reduces overall MoE layer latency and better utilizes the Cube unit and vector unit concurrently.

## Related
- `kernel-moe-ascendc`, `technique-pipeline-scheduling`, `technique-cube-vector-overlap`