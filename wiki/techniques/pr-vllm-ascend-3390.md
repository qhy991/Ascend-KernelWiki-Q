---
id: technique-pr-vllm-ascend-3390
title: "PR Insight: vllm-project/vllm-ascend #3390"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - attention
  - hccl-optimization
  - aclgraph
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3390"
---

# PR Insight: vllm-project/vllm-ascend #3390

**Title:** add new accuracy test case for aclgraph

## Overview
Add new accuracy test case Deepseek-V2-Lite-W8A8 for aclgraph

## Technical Significance
Adds new accuracy test cases for ACLGraph mode to ensure correctness of graph-compiled operators.

## Related
- `hw-cube-unit`
- `technique-aclgraph`
