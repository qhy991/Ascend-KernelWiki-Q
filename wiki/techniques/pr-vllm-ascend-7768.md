---
id: technique-pr-vllm-ascend-7768
title: "PR Insight: vllm-project/vllm-ascend #7768"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - fused-moe
  - testing
  - unit-test
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7768"
---

# PR Insight: vllm-project/vllm-ascend #7768

**Title:** [Test] Spplement UT for ops - fused moe

## Overview
This PR supplements unit tests for fused MoE operations, adding test coverage for fused_moe and select_experts operators. The tests validate correctness of MoE fusion and expert selection operations.

## Technical Significance
Improves test coverage for MoE operations, ensuring correctness of fused MoE kernels and expert selection logic across different configurations and workloads.

## Related
- `kernel-moe`, `technique-operator-fusion`, `pattern-moe-routing`, `technique-testing-coverage`, `pattern-expert-selection`