---
id: technique-pr-vllm-ascend-6844
title: "PR Insight: vllm-project/vllm-ascend #6844"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - pipeline-scheduling
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6844"
---

# PR Insight: vllm-project/vllm-ascend #6844

**Title:** [Perf] Optimize MTP execution by reordering state update operation

## Overview
Optimizes MTP (Multi-Token Prediction) performance by reordering the `_update_states_after_model_execute` call from after main model sampling to after draft model execution. This reordering reduces pipeline bubbles between main and draft model execution stages without affecting accuracy.

## Technical Significance
Improves MTP throughput by eliminating idle time between main model and draft model execution stages. The state update operation is independent of draft token proposal, allowing safe reordering that reduces pipeline stalls and increases overall speculative decoding efficiency.

## Related
- `technique-mtp`, `technique-pipeline-scheduling`, `technique-spec-decode`