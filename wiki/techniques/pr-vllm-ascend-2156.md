---
id: technique-pr-vllm-ascend-2156
title: "PR Insight: vllm-project/vllm-ascend #2156"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - moe
  - configuration
  - torchair
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2156"
---

# PR Insight: vllm-project/vllm-ascend #2156

**Title:** [Fix] Adjust use_aclgraph logic

## Overview
This PR updates the FusedMoE method to determine whether to use ACL Graph based on the `torchair_graph_config` configuration. The modification adds 10 lines to `vllm_ascend/ops/common_fused_moe.py` and 1 line to `vllm_ascend/ops/fused_moe.py`.

## Technical Significance
This fix ensures proper decision logic for when to enable ACL Graph mode in MoE layers. By checking the torchair configuration rather than hardcoded conditions, the system can dynamically adapt to user preferences and deployment scenarios. This is a port of equivalent PR #2154 on v0.9.1-dev to the main branch.

## Related
- `technique-aclgraph-integration`, `kernel-fused-moe-ascendc`, `technique-torchair-configuration`