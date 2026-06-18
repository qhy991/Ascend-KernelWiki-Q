---
id: technique-pr-vllm-ascend-2437
title: "PR Insight: vllm-project/vllm-ascend #2437"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pangu-moe
  - torchair
  - refactor
  - modeling
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2437"
---

# PR Insight: vllm-project/vllm-ascend #2437

**Title:** [1/N][Draft][Refactor]torchair pangu_moe modeling refactor

## Overview
This PR adds TorchAir-specific modeling for Pangu-MoE, similar to the approach in PR #2384. It also fixes a bug introduced by routed_scaling_factor in PR #2675 and removes eager test cases for Pangu since TorchAir test cases already exist. The implementation creates `vllm_ascend/torchair/models/torchair_pangu_moe.py` (1119 lines) and updates related files.

## Technical Significance
This refactoring isolates TorchAir-specific Pangu-MoE modeling into a dedicated module, improving code organization and maintainability. The bugfix for routed_scaling_factor ensures correct MoE behavior, and removing duplicate tests reduces test maintenance burden.

## Related
- `kernel-fused-moe-ascendc`, `kernel-pangu-moe`, `technique-torchair-integration`, `technique-code-refactor`