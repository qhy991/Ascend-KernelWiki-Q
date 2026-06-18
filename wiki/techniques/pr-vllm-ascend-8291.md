---
id: technique-pr-vllm-ascend-8291
title: "PR Insight: vllm-project/vllm-ascend #8291"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pd-separation
  - deepseek-v3.2
  - bugfix
  - dsa-cp
  - role-gating
  - fc1
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8291"
---

# PR Insight: vllm-project/vllm-ascend #8291

**Title:** [BugFix][DSv32] Fix DSA-CP PD role gating for deepseek v3.2 (v0.18.0)

## Overview
This PR backports the DSA-CP PD role gating fix from #8290 to the v0.18.0 release branch. The existing helper logic on the release branch did not handle PD mixed-role cases correctly when deciding whether layer sharding or TP o_proj handling should be enabled. The fix makes those conditions explicit and adds unit coverage for allowed and disallowed combinations.

## Technical Significance
This cherry-pick ensures consistency between main and release branches for PD separation role gating logic. The fix prevents vllm serve failures in specific DeepSeek v3.2 configurations by ensuring correct role-based feature enablement. The backport maintains reliability across different vLLM versions for PD-separated deployments.

## Related
- `technique-pd-separation`
- `technique-kv-pooling`
- `technique-role-gating`