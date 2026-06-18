---
id: technique-pr-vllm-ascend-682
title: "PR Insight: vllm-project/vllm-ascend #682"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - deepseek
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/682"
---

# PR Insight: vllm-project/vllm-ascend #682

**Title:** [Bugfix] Fix early return in CustomDeepseekV2MoE.forward during profile_run

## Overview
This PR fixes an early return bug in CustomDeepseekV2MoE.forward during profiling runs. The change modifies deepseek_v2.py (5 additions, 5 deletions).

## Technical Significance
Profile runs measure performance for optimization. Early returns during profiling prevent accurate measurements. The fix ensures MoE layers are properly profiled for performance tuning.

## Related
- kernel-moe
- technique-deepseek