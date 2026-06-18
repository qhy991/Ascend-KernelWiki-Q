---
id: technique-pr-vllm-ascend-8483
title: "PR Insight: vllm-project/vllm-ascend #8483"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - gemm
  - unquantized
  - custom-op
  - refactoring
  - monkey-patch
  - dispatch
  - privateuse1
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8483"
---

# PR Insight: vllm-project/vllm-ascend #8483

**Title:** [Refactor] Replace unquantized_gemm monkey-patch with proper custom op dispatch

## Overview
This PR refactors the unquantized_gemm custom operator registration by moving it from patch_unquantized_gemm.py into AscendUnquantizedLinearMethod.apply() in ops/linear.py, using the PrivateUse1 dispatch key. This removes the need for runtime monkey-patching on vllm.model_executor.layers.utils.default_unquantized_gemm. The PR also updates allreduce_rmsnorm_fusion_pass.py to use maybe_chunk_residual in pattern matching.

## Technical Significance
Replacing monkey-patching with proper custom op dispatch improves code maintainability and reduces runtime overhead. The PrivateUse1 dispatch key provides a cleaner mechanism for custom operator registration. This refactoring demonstrates best practices for integrating custom operators without relying on runtime patching, which can be fragile and hard to debug.

## Related
- `kernel-gemm-ascendc`
- `technique-custom-operator`
- `technique-refactoring`