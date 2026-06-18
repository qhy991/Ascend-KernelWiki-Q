---
id: technique-pr-vllm-ascend-8290
title: "PR Insight: vllm-project/vllm-ascend #8290"
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
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8290"
---

# PR Insight: vllm-project/vllm-ascend #8290

**Title:** [BugFix][DSv32] Fix DSA-CP PD role gating for deepseek v3.2

## Overview
This PR fixes DSA-CP PD (Prefill-Decode) role gating logic in vllm_ascend.utils that did not correctly distinguish PD mixed-role cases when deciding whether layer sharding or TP o_proj handling should be enabled. The incorrect condition led to vllm serve failures in specific configurations: FC1 + PD-colocated KV pooling + no layer_sharding, causing insufficient available KV cache memory and o_proj shape errors.

## Technical Significance
This fix is critical for correct DeepSeek v3.2 deployment with PD separation and KV pooling. The role gating logic ensures that layer sharding only runs on P-side instances while TP o_proj handling remains enabled for normal deployments and PD mixed-role instances. The PR adds explicit condition checks and unit coverage to prevent similar deployment failures.

## Related
- `technique-pd-separation`
- `technique-kv-pooling`
- `technique-role-gating`