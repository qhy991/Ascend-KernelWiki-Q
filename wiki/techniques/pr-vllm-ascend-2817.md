---
id: technique-pr-vllm-ascend-2817
title: "PR Insight: vllm-project/vllm-ascend #2817"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - bugfix
  - shared-moe
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2817"
---

# PR Insight: vllm-project/vllm-ascend #2817

**Title:** [Fix] Fix SharedFusedMoE

## Overview
This PR fixes a bug in the SharedFusedMoE implementation, addressing issues in the common_fused_moe.py and related platform patching code for shared MoE scenarios.

## Technical Significance
Bug fix for SharedFusedMoE, which is critical for models that use shared expert weights across different routing configurations. The fix ensures correct behavior when MoE operators share weights or when using expert parallelism, preventing potential incorrect computations or memory access issues.

## Related
- `kernel-moe-ascendc`, `technique-moe-optimization`