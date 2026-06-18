---
id: technique-pr-vllm-ascend-4850
title: "PR Insight: vllm-project/vllm-ascend #4850"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - sfa
  - cp
  - multi-dp
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4850"
---

# PR Insight: vllm-project/vllm-ascend #4850

**Title:** [Bugfix] Fix the bug in sfa-cp under multi-DP scenarios.

## Overview
This PR fixes a bug in SFA (Sparse Flash Attention) with context parallelism (CP) when running in multi-data-parallel (DP) scenarios. The fix is applied to vllm_ascend/attention/sfa_v1.py.

## Technical Significance
Resolves incorrect behavior in SFA-CP when multiple DP groups are present. Ensures correct attention computation when combining context and data parallelism strategies.

## Related
- `kernel-sfa`
- `technique-context-parallelism`
- `kernel-attention-sfa`