---
id: technique-pr-vllm-ascend-5836
title: "PR Insight: vllm-project/vllm-ascend #5836"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - eplb
  - bugfix
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5836"
---

# PR Insight: vllm-project/vllm-ascend #5836

**Title:** [v0.13.0][cherry-pick][Bugfix] Fix acc bug when enbale dispatch_gmm_combine_decode and eplb

## Overview
This is a cherry-pick of PR #5806 for the v0.13.0 release branch. It fixes the same accuracy bug in the fused_moe operator when both dispatch_gmm_combine_decode and EPLB are enabled. The issue occurs because expert table changes after EPLB require proper mapping that was missing in the fused_mc2 operator.

## Technical Significance
This fix ensures the v0.13.0 branch maintains correctness for MoE models with expert parallel load balancing. Without this fix, models like Qwen3-235B with EPLB and dispatch_gmm_combine_decode would suffer severe accuracy degradation. The cherry-pick applies the same expert mapping fix to the release branch, maintaining parity with the main branch's correctness.

## Related
- `technique-pr-vllm-ascend-5806`, `technique-moe-dispatch`, `technique-eplb`