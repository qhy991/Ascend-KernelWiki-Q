---
id: technique-pr-vllm-ascend-5512
title: "PR Insight: vllm-project/vllm-ascend #5512"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - revert
  - bugfix
  - aclnn
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5512"
---

# PR Insight: vllm-project/vllm-ascend #5512

**Title:** Revert "moe_gating_top_k"

## Overview
This PR reverts PR #5271 which added the moe_gating_top_k operator. The revert was necessary because the implementation broke end-to-end tests, indicating correctness or compatibility issues with the new operator.

## Technical Significance
The removal of the moe_gating_top_k operator demonstrates the importance of thorough testing for complex MoE routing operations. The operator was intended to optimize MoE expert selection performance, but correctness issues led to its removal, highlighting the trade-offs between optimization and reliability in kernel development.

## Related
- `pattern-moe` (MoE patterns and operations)
- `kernel-moe` (MoE gating operations)
- `technique-operator-development` (Custom operator development)