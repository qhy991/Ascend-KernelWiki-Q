---
id: technique-pr-vllm-ascend-2791
title: "PR Insight: vllm-project/vllm-ascend #2791"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - communication
  - allgather
  - quantization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2791"
---

# PR Insight: vllm-project/vllm-ascend #2791

**Title:** [Main] [Refactor] Enable MoECommMethod in Eager Mode

## Overview
This PR refactors MoE communication to enable MoECommMethod in eager mode, replacing custom prepare/finalize operations with standardized moe_comm_method interfaces. It updates fused_moe.py, w8a8_dynamic.py, and w4a8_dynamic.py to use unified communication patterns, and disables AllgatherEP in aclgraph/eager mode following model runner rules.

## Technical Significance
Unifies MoE communication patterns across different execution modes (aclgraph and eager), improving code maintainability and ensuring consistent behavior. The refactoring enables proper communication method selection, with w4a8_dynamic using all2allv instead of gatherep. This is critical for MoE model performance and correctness on Ascend NPUs.

## Related
- `technique-moe-optimization`, `technique-hccl-optimization`, `kernel-moe-ascendc`