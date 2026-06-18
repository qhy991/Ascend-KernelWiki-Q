---
id: technique-pr-vllm-ascend-6760
title: "PR Insight: vllm-project/vllm-ascend #6760"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - eager-mode
  - aclgraph
  - piecewise
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6760"
---

# PR Insight: vllm-project/vllm-ascend #6760

**Title:** [Bugfix] mtp forces eager mode

## Overview
This PR forces MTP (Multi-Token Proposal) to use eager mode by setting use_cuda_graph to false. This is necessary because async_scheduler is enabled by default and MTP doesn't need ACLGraph, while piecewise execution with MTP could cause unexpected errors with ACLGraph enabled.

## Technical Significance
Prevents unexpected errors in MTP speculative decoding by enforcing eager mode execution. This ensures consistent behavior across different execution modes and graph compilation scenarios.

## Related
- `technique-speculative-decoding`