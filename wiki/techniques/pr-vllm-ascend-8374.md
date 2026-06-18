---
id: technique-pr-vllm-ascend-8374
title: "PR Insight: vllm-project/vllm-ascend #8374"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pd-separation
  - scheduling
  - recompute
  - balance
  - mc2
  - bugfix
  - feature-gate
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8374"
---

# PR Insight: vllm-project/vllm-ascend #8374

**Title:** [BugFix][v0.18.0] Gate recompute/balance/fused_mc2 by PD mode

## Overview
This PR backports the PD mode feature gating fix from #8373 to the v0.18.0 release branch. It enforces feature gating based on PD separation mode: recompute scheduling only in PD-disaggregated mode, balance scheduling only in PD-mixed mode, and fused MC2 only on PD-disaggregated D-side (kv_consumer). The changes ensure proper feature enablement across vLLM versions.

## Technical Significance
This cherry-pick ensures consistency between main and release branches for PD mode-aware feature gating. Correct feature enablement is critical for avoiding performance degradation or functional issues in different PD configurations. Maintaining the fix across release branches ensures reliable behavior for users on different vLLM versions.

## Related
- `technique-pd-separation`
- `technique-scheduling-optimization`
- `technique-feature-gating`