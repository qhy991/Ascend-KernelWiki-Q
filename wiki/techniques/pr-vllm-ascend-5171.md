---
id: technique-pr-vllm-ascend-5171
title: "PR Insight: vllm-project/vllm-ascend #5171"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - dispatch
  - token-masking
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5171"
---

# PR Insight: vllm-project/vllm-ascend #5171

**Title:** [Feature] Add token mask for DispatchGmmCombineDecode operator

## Overview
This PR adds an optional `x_active_mask` input to the DispatchGmmCombineDecode operator, enabling selective token processing. Only tokens marked as active (mask=True) are dispatched and processed through the MoE expert dispatch and combine pipeline.

## Technical Significance
Token masking enables conditional computation in MoE models, allowing selective token routing based on relevance scores. This optimization reduces unnecessary computation for inactive tokens, improving MoE inference efficiency on Ascend NPUs during decode stages.

## Related
- technique-moe
- technique-conditional-computation
- technique-token-filtering