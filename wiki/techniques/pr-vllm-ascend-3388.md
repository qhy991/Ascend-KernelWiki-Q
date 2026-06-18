---
id: technique-pr-vllm-ascend-3388
title: "PR Insight: vllm-project/vllm-ascend #3388"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - hccl-optimization
  - aclgraph
  - decode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3388"
---

# PR Insight: vllm-project/vllm-ascend #3388

**Title:** ACLgraph enable: Test cases revisions for all features

## Overview
This PR revise the test cases of various features on the warehouse which add the enablement of aclgraph to the test cases.

## Technical Significance
Enables ACLGraph compilation and revises test cases to validate all feature combinations in graph mode.

## Related
- `technique-aclgraph`
