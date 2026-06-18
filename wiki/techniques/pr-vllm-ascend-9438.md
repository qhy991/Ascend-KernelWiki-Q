---
id: technique-pr-vllm-ascend-9438
title: "PR Insight: vllm-project/vllm-ascend #9438"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - swiglu
  - clamp
  - bugfix
  - moe
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9438"
---

# PR Insight: vllm-project/vllm-ascend #9438

**Title:** [Ops][BugFix] Disable SwiGLU clamp by default

## Overview
This PR disables SwiGLU activation clamping by default across multiple operators including GMM SwiGLU quantization, SwiGLU quantization V2, and dequant SwiGLU quantization. The changes affect operator definitions, tiling logic, kernel implementations, and torch bindings.

## Technical Significance
SwiGLU clamping can be necessary for numerical stability in some cases but may also limit performance or accuracy in others. Disabling it by default provides better baseline behavior while still allowing it to be enabled when needed through configuration.

## Related
- `kernel-moe`
- `hw-cube-unit`