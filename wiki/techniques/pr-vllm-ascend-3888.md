---
id: technique-pr-vllm-ascend-3888
title: "PR Insight: vllm-project/vllm-ascend #3888"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - testing
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3888"
---

# PR Insight: vllm-project/vllm-ascend #3888

**Title:** add new test model for aclgraph single_request

## Overview
This PR adds new test models for ACLGraph single request scenarios in multi-card testing. The changes expand test coverage for ACLGraph functionality when processing single requests across multiple Ascend NPUs, ensuring graph mode correctness in distributed inference scenarios.

## Technical Significance
Testing single request behavior in multi-card ACLGraph mode is important for validating that graph capture and replay work correctly when requests are distributed across multiple devices. This test coverage helps ensure that ACLGraph optimization doesn't introduce correctness issues in tensor parallel or distributed inference scenarios.

## Related
- `technique-aclgraph`, `technique-distributed-inference`, `technique-tensor-parallel`