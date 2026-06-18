---
id: technique-pr-vllm-ascend-1759
title: "PR Insight: vllm-project/vllm-ascend #1759"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - dbo
  - multistream
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1759"
---

# PR Insight: vllm-project/vllm-ascend #1759

**Title:** [BugFix] Fix the bug when enabling both DBO and MoE multistream of deepseek.

## Overview
This PR fixes a compatibility issue when both DBO (Dynamic Batch Optimization) and MoE multistream are enabled for DeepSeek models. The fix is implemented in `vllm_ascend/models/deepseek_dbo.py` and includes end-to-end unit tests for the scenario.

## Technical Significance
Critical bugfix for combined optimization features. DBO and MoE multistream are both performance features, and their interaction requires careful coordination to avoid conflicts in expert routing and token management.

## Related
- `technique-moe`
- `technique-multistream`
- `technique-dbo`
- `technique-deepseek`