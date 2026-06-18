---
id: technique-pr-vllm-ascend-6363
title: "PR Insight: vllm-project/vllm-ascend #6363"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - moe
  - shared-experts
  - tensor-parallel
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6363"
---

# PR Insight: vllm-project/vllm-ascend #6363

**Title:** [cherry-pick][BugFix] Disable enable_shared_expert_dp by default if tensor_parallel_size=1

## Overview
This is a cherry-pick of PR #6361 to the 0.13.0 branch, applying the same fix to disable shared expert data parallelism by default for single-card tensor parallelism.

## Technical Significance
Same as PR #6361 - prevents unnecessary overhead in single-card MoE inference on the 0.13.0 release branch by not enabling shared expert DP when it provides no benefit.

## Related
- `technique-moe`
- `technique-shared-experts`
- `technique-tensor-parallel`