---
id: technique-pr-vllm-ascend-10553
title: "PR Insight: vllm-project/vllm-ascend #10553"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - operator-fusion
  - ascendc
  - gdn
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10553"
---

# PR Insight: vllm-project/vllm-ascend #10553

**Title:** [Refactor][Op] Align fused_gdn_gating API and softplus semantics

## Overview
This PR aligns the AscendC `fused_gdn_gating` operator implementation with the Triton reference implementation. It adds the `softplus_threshold` parameter through the full AscendC op stack, updates the softplus computation to match Triton semantics, and supports fp32/bf16/fp16 `A_log` and `dt_bias` inputs while keeping the actual computation in fp32. The changes span the operator definition, tiling, kernel implementation, and Python bindings, ensuring consistency across the entire operator stack.

## Technical Significance
This refactoring ensures that the AscendC implementation of `fused_gdn_gating` provides the same semantics and functionality as the Triton reference. The alignment is critical for model correctness, especially for architectures that rely on GDN (Gated Down-projection Network) operations. Supporting multiple input dtypes while maintaining fp32 computation precision ensures flexibility and accuracy. The comprehensive changes across the operator stack demonstrate the importance of maintaining consistency from Python bindings down to kernel implementation.

## Related
- `technique-operator-fusion`
- `technique-ascendc`
- `technique-gdn`