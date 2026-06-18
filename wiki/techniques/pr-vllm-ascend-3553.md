---
id: technique-pr-vllm-ascend-3553
title: "PR Insight: vllm-project/vllm-ascend #3553"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - fia
  - attention
  - accuracy
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3553"
---

# PR Insight: vllm-project/vllm-ascend #3553

**Title:** Revert "[Perf] Add FIA interface in FA case"

## Overview
This PR reverts the FIA (Flash-Inference-Attention) interface optimization from PR #3321 due to output dimension mismatches and accuracy issues. The revert affects `vllm_ascend/attention/attention_v1.py` and `vllm_ascend/worker/model_runner_v1.py`, removing 44 lines of optimization code and adding back 12 lines of previous implementation.

## Technical Significance
The FIA interface was intended to improve attention performance but introduced dimension mismatches that caused accuracy degradation. This revert highlights the trade-off between kernel-level optimizations and correctness, particularly for attention mechanisms where output tensor dimensions must exactly match expected shapes. The FIA optimization approach may need refinement before re-introduction.

## Related
- `technique-flash-attention`
- `technique-operator-fusion`
- `hw-attention`