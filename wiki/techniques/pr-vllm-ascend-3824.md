---
id: technique-pr-vllm-ascend-3824
title: "PR Insight: vllm-project/vllm-ascend #3824"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - deepseek
  - allgather
  - gate
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3824"
---

# PR Insight: vllm-project/vllm-ascend #3824

**Title:** [Bugfix] [MoE] fix error in deepseek when using allgather

## Overview
This PR fixes an error in DeepSeek models when using allgather for MoE communication. After refactoring models and FusedMoE, the `gate` parameter couldn't be passed from `deepseekv2.py` to `AscendFusedMoE.forward`, causing failures. The fix removes gate-related computations from FusedMoE module in eager/aclgraph mode and deprecates `rm_router_logits` in those modes.

## Technical Significance
The refactoring introduced incompatibility with allgather communication patterns used in DeepSeek MoE. Removing gate computations from FusedMoE in eager/aclgraph modes ensures compatibility while maintaining functionality in torchair mode. This fix is critical for DeepSeek V3/R1 inference with allgather-based expert communication.

## Related
- `technique-moe`
- `technique-allgather`
- `technique-deepseek`