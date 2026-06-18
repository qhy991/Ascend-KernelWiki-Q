---
id: technique-pr-vllm-ascend-5806
title: "PR Insight: vllm-project/vllm-ascend #5806"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - eplb
  - expert-parallel
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5806"
---

# PR Insight: vllm-project/vllm-ascend #5806

**Title:** [Bugfix] Fix acc bug when enbale dispatch_gmm_combine_decode and eplb

## Overview
This PR fixes a critical accuracy bug in the fused_moe operator when both dispatch_gmm_combine_decode and EPLB (Expert Parallel Load Balancing) are enabled. After EPLB optimization, the expert table may change, requiring proper mapping logic that was missing in the fused_mc2 operator implementation. The fix adds the necessary expert mapping to ensure correct expert-to-token routing.

## Technical Significance
This PR addresses a correctness issue in MoE routing under expert parallel scenarios. Without this fix, Qwen3-235B models with EPLB and dispatch_gmm_combine_decode would achieve only 3.33% accuracy on AIME2024 benchmarks. After the fix, accuracy is restored to 86.67%, matching the baseline without dispatch_gmm_combine_decode. The fix ensures that expert table changes due to EPLB are properly tracked and applied to the fused_moe kernel.

## Related
- `technique-moe-dispatch`, `technique-expert-parallel`, `technique-eplb`