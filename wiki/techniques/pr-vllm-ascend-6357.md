---
id: technique-pr-vllm-ascend-6357
title: "PR Insight: vllm-project/vllm-ascend #6357"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - fia-operator
  - tnd-layout
  - attention
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6357"
---

# PR Insight: vllm-project/vllm-ascend #6357

**Title:** [Fix] Pads query_start_loc to satisfy FIA/TND constraint

## Overview
This PR adds padding logic for `query_start_loc` to satisfy FIA/TND layout constraints in full graph modes. The fix handles both uniform and mixed batches by inserting dummy requests when needed, and consolidates ad-hoc padding into a single helper function in `vllm_ascend/worker/model_runner_v1.py`.

## Technical Significance
The padding ensures correct tensor shapes for FIA/TND execution, preventing kernel mismatches or failures. This is critical for stable operation in full graph modes with mixed batch types and maintains compatibility with CANN's layout requirements.

## Related
- `technique-fia-operator`
- `technique-tnd-layout`
- `technique-attention`
- `technique-full-graph`