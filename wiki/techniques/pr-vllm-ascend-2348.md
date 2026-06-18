---
id: technique-pr-vllm-ascend-2348
title: "PR Insight: vllm-project/vllm-ascend #2348"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - bugfix
  - initialization
  - quickfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2348"
---

# PR Insight: vllm-project/vllm-ascend #2348

**Title:** [Quickfix] Add the missing `apply_router_weight_on_input` in FusedMoE init

## Overview
This PR is a quick fix that adds the missing `apply_router_weight_on_input` parameter in the FusedMoE initialization. The change is minimal (1 line added to `vllm_ascend/ops/fused_moe.py`) but addresses an issue where this parameter was not being properly passed through.

## Technical Significance
This bugfix ensures that the router weight application configuration is properly initialized in FusedMoE, preventing potential errors or incorrect behavior when this parameter is needed for specific MoE configurations. The fix maintains consistency with expected MoE initialization parameters.

## Related
- `kernel-fused-moe-ascendc`, `technique-moe-initialization`, `technique-bugfix`