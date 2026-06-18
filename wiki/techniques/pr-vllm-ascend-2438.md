---
id: technique-pr-vllm-ascend-2438
title: "PR Insight: vllm-project/vllm-ascend #2438"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - fused-moe
  - torchair
  - refactor
  - code-organization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2438"
---

# PR Insight: vllm-project/vllm-ascend #2438

**Title:** [1/N][refactor] torchair fused_moe refactor

## Overview
This PR refactors torchair-related fused_moe code by moving it into a dedicated `torchair_fused_moe` module. The implementation creates `vllm_ascend/torchair/ops/torchair_fused_moe.py` (1570 lines) to separate torchair-specific logic from the general fused_moe implementation.

## Technical Significance
This refactoring improves code clarity and maintainability by isolating TorchAir-specific MoE implementation into its own module. The next steps will remove all torchair-related code from outside the torchair_fused_moe module, further improving code organization and reducing coupling between different execution backends.

## Related
- `kernel-fused-moe-ascendc`, `technique-torchair-integration`, `technique-code-refactor`, `technique-module-separation`