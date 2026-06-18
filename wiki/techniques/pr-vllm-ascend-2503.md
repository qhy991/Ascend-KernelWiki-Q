---
id: technique-pr-vllm-ascend-2503
title: "PR Insight: vllm-project/vllm-ascend #2503"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - fused-moe
  - torchair
  - refactor
  - separation
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2503"
---

# PR Insight: vllm-project/vllm-ascend #2503

**Title:** [2/N][refactor] split torchair from fused_moe

## Overview
This PR continues the torchair refactoring by splitting torchair-specific code from the general fused_moe implementation, following the work in PR #2438 where torchair code was moved to torchair_fused_moe. The implementation adds 16 lines and removes 47 lines from `vllm_ascend/ops/fused_moe.py`.

## Technical Significance
This refactoring completes the separation of torchair and non-torchair MoE code paths, improving code organization and maintainability. The cleaner separation makes it easier to evolve each backend independently and reduces the risk of unintended interactions between different execution modes.

## Related
- `kernel-fused-moe-ascendc`, `technique-torchair-integration`, `technique-code-refactor`, `technique-backend-separation`