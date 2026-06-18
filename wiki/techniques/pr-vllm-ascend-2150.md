---
id: technique-pr-vllm-ascend-2150
title: "PR Insight: vllm-project/vllm-ascend #2150"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - refactor
  - experts-selector
  - code-organization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2150"
---

# PR Insight: vllm-project/vllm-ascend #2150

**Title:** refactor select_experts of moe module

## Overview
This PR refactors the expert selection logic in MoE modules by merging quantization and non-quantization implementations into a new `ExpertsSelector` class. Changes include creating `vllm_ascend/ops/layers/experts_selector.py` (269 lines), removing significant code from `vllm_ascend/ops/fused_moe.py` (167 deletions), and simplifying quantization files `vllm_ascend/quantization/w4a8_dynamic.py`, `w8a8.py`, and `w8a8_dynamic.py`.

## Technical Significance
This consolidation improves code maintainability by using a unified API (`ExpertsSelector.select_experts`) similar to vLLM's approach, eliminating code duplication between quantization and non-quantization paths. The refactoring simplifies the codebase and makes it easier to maintain and extend expert selection logic across different quantization schemes.

## Related
- `kernel-fused-moe-ascendc`, `technique-expert-selection`, `technique-code-refactor`