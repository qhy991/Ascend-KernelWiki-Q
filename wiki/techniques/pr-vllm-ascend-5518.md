---
id: technique-pr-vllm-ascend-5518
title: "PR Insight: vllm-project/vllm-ascend #5518"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - triton
  - operator-fusion
  - compilation
  - refactoring
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5518"
---

# PR Insight: vllm-project/vllm-ascend #5518

**Title:** [Triton][Config] Add muls_add triton kernel and refactor AscendCompilationConfig

## Overview
This PR adds a muls_add Triton kernel with corresponding fusion pass and refactors the compilation configuration system by consolidating `AscendCompilationConfig` and removing `NpugraphExConfig`. The new fusion pass enables optimization of multiply-add operations on Ascend NPU.

## Technical Significance
The muls_add fusion kernel reduces memory traffic and kernel launch overhead by combining multiple multiplication and addition operations into a single fused Triton kernel. The configuration refactoring simplifies the compilation system architecture, making it easier to maintain and extend with new fusion passes and operators.

## Related
- `technique-triton` (Triton kernel development)
- `technique-operator-fusion` (Multiply-add fusion)
- `technique-compilation` (Graph compilation system)
- `kernel-arithmetic` (Elementwise operations)