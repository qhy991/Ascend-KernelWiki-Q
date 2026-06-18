---
id: technique-pr-vllm-ascend-2569
title: "PR Insight: vllm-project/vllm-ascend #2569"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - torchair
  - quantization
  - w8a8
  - w4a8
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2569"
---

# PR Insight: vllm-project/vllm-ascend #2569

**Title:** [bugfix][refactor]fix torchair_w8a8

## Overview
This PR refactors and fixes torchair W8A8 and W4A8 dynamic quantization implementations by separating them from the fused_moe module. The changes update both `torchair_w4a8_dynamic.py` and `torchair_w8a8_dynamic.py` to work independently following the fused_moe refactoring.

## Technical Significance
The refactoring separates quantization operations from the fused_moe implementation to improve code organization and maintainability. This decoupling allows for independent evolution of quantization schemes and MoE fusion, preventing potential issues when one component changes. The fix ensures torchair quantization operations work correctly after the fused_moe refactoring.

## Related
- `technique-quantization`
- `technique-fused-moe`
- `technique-w8a8`