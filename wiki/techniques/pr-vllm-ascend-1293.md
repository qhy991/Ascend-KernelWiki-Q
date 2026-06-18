---
id: technique-pr-vllm-ascend-1293
title: "PR Insight: vllm-project/vllm-ascend #1293"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - ci
  - moe
  - testing
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1293"
---

# PR Insight: vllm-project/vllm-ascend #1293

**Title:** [UT] refactor test_expert_load_balancer and fix broken CI

## Overview
This PR refactors the expert load balancer unit tests and fixes broken CI pipelines. The refactoring improves test coverage and stability for MoE load balancing mechanisms.

## Technical Significance
Improves CI reliability for MoE inference workflows by refactoring `test_expert_load_balancer.py` and fixing scheduler tests. The changes touch core scheduling components and model runner V1, ensuring that expert load balancing logic is correctly tested and CI failures are resolved. This is essential for maintaining quality assurance for distributed MoE inference on Ascend.

## Related
- `kernel-moe`
- `technique-load-balancing`