---
id: technique-pr-vllm-ascend-3392
title: "PR Insight: vllm-project/vllm-ascend #3392"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - hccl-optimization
  - aclgraph
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3392"
---

# PR Insight: vllm-project/vllm-ascend #3392

**Title:** add single request test case for aclgraph

## Overview
This pr adds online single request DP2 test case for aclgraph

## Technical Significance
Adds single request test cases for ACLGraph to validate graph capture behavior in single-request scenarios.

## Related
- `technique-aclgraph`
