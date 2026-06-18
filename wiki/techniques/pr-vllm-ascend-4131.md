---
id: technique-pr-vllm-ascend-4131
title: "PR Insight: vllm-project/vllm-ascend #4131"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - testing
  - bugfix
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4131"
---

# PR Insight: vllm-project/vllm-ascend #4131

**Title:** [Fix] fix aclgraph e2e test.

## Overview
This PR fixes ACLGraph end-to-end tests by modifying them to compare with given outputs instead of checking for exact equality. The change addresses the issue where different attention operators used in eager mode vs graph mode have non-deterministic accumulation orders, making exact equality comparisons unreliable.

## Technical Significance
Non-deterministic accumulation in different attention operators is expected behavior due to parallel execution and numerical precision differences. The fix ensures tests are robust to these expected differences while still validating correctness by comparing to reference outputs. This is critical for maintaining test reliability across different execution modes.

## Related
- `technique-aclgraph`, `technique-attention`, `pattern-testing`, `technique-numerical-stability`