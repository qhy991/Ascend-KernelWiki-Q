---
id: technique-pr-vllm-ascend-5698
title: "PR Insight: vllm-project/vllm-ascend #5698"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - sfa
  - sharded-cp
  - custom-op
  - linear-op
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5698"
---

# PR Insight: vllm-project/vllm-ascend #5698

**Title:** [Refactor] Replace the implementations of o_proj, q_b_proj, and kv_b_proj with custom_op for sharded CP

## Overview
This PR refactors the Sharded-CP feature by replacing the implementations of o_proj, q_b_proj, and kv_b_proj with custom operators, extracted from PR #5513. The changes affect SFA v1 attention and linear operation implementations.

## Technical Significance
Refactoring to custom operators improves integration with vLLM's operator framework and enables better optimization opportunities. Custom operators allow for proper graph compilation, operator fusion, and performance optimization in aclgraph mode, which is critical for the Sharded-CP feature's performance.

## Related
- `kernel-attention-ascendc`, `technique-sfa`, `technique-sharded-cp`