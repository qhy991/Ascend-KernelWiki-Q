---
id: technique-pr-vllm-ascend-3001
title: "PR Insight: vllm-project/vllm-ascend #3001"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - comm-method
  - refactoring
  - qwen3
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3001"
---

# PR Insight: vllm-project/vllm-ascend #3001

**Title:** [Refactor] Adjustments to moe_comm_method selection process

## Overview
This PR refactors the MoE communication method selection process by using Enum instead of strings, avoiding setting new properties in forward_context, enabling TokenDispatcherWithMoGE, and removing redundant code. It addresses issues from PR #2791 and improves code maintainability.

## Technical Significance
The refactoring improves code quality and performance by eliminating redundant operations and using type-safe Enums. Enabling TokenDispatcherWithMoGE provides better token dispatching for MoE models, improving load balancing and communication efficiency across different expert parallelism configurations.

## Related
- `kernel-moe-ascendc`, `technique-moe-communication`, `pattern-moe-dispatch`