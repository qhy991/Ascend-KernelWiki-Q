---
id: technique-pr-vllm-ascend-1267
title: "PR Insight: vllm-project/vllm-ascend #1267"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - rotary-embedding
  - bugfix
  - attention
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1267"
---

# PR Insight: vllm-project/vllm-ascend #1267

**Title:** [Bugfix] fix rope sin/cos cache bug

## Overview
This PR is a cherry-pick of #1266 to the v0.9.1-dev branch, fixing the same rotary embedding sin/cos cache allocation bug for maintenance releases.

## Technical Significance
Backports the RoPE cache dimensionality fix to ensure consistency across all vLLM Ascend release branches. The cherry-pick maintains the same fix logic from the main branch, ensuring that deployments on v0.9.1-dev also benefit from correct rotary embedding cache allocation for long sequences.

## Related
- `technique-rotary-embedding`
- `kernel-attention`