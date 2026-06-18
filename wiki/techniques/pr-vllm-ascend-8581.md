---
id: technique-pr-vllm-ascend-8581
title: "PR Insight: vllm-project/vllm-ascend #8581"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - gdn
  - attention
  - refactoring
  - qwen3.5
  - recurrent
  - accuracy
  - misc
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8581"
---

# PR Insight: vllm-project/vllm-ascend #8581

**Title:** [Ops][Misc] Refactor GDN recurrent attention logic

## Overview
This PR refactors the _forward_core method in vllm_ascend/ops/gdn.py to unify the recurrent attention logic by removing layout-specific branching. The simplification ensures that gating parameters are computed and applied consistently using the npu_recurrent_gated_delta_rule operator. The PR also fixes accuracy problems in non-MTP scenes of the qwen3.5 model, with GSM8K dataset showing 96.97% accuracy regardless of MTP enablement.

## Technical Significance
The refactoring simplifies GDN implementation by removing layout-specific code paths, improving maintainability and reducing potential bugs. The accuracy fix ensures consistent model performance across different deployment configurations (with/without MTP). Unifying the logic using the NPU operator ensures correct gating parameter computation in all scenarios.

## Related
- `technique-gdn-attention`
- `technique-refactoring`
- `technique-recurrent-attention`