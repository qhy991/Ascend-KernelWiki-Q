---
id: technique-pr-vllm-ascend-7674
title: "PR Insight: vllm-project/vllm-ascend #7674"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - moe
  - operator-fusion
  - qwen3.5
  - shared-experts
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7674"
---

# PR Insight: vllm-project/vllm-ascend #7674

**Title:** [Feature][310P] support shared experts path in fused MoE for qwen3.5

## Overview
This PR adds shared experts path support to fused MoE operations for Qwen3.5 models on Ascend 310P. It modifies the fused MoE implementation and Qwen3.5 patching to handle shared expert routing efficiently.

## Technical Significance
Enables efficient shared expert processing in MoE models like Qwen3.5 on Ascend 310P, reducing computational overhead by fusing shared expert operations with the main MoE computation path.

## Related
- `kernel-moe`, `technique-operator-fusion`, `pattern-qwen-architecture`, `technique-moe-optimization`