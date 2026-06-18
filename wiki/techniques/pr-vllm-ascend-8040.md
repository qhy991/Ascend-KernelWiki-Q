---
id: technique-pr-vllm-ascend-8040
title: "PR Insight: vllm-project/vllm-ascend #8040"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - mc2
  - hccl
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8040"
---

# PR Insight: vllm-project/vllm-ascend #8040

**Title:** [releases/v0.18.0][BugFix] Restore global_bs=0 and mc2_mask for uniform-token dispatching and support inter-node roce hierarchical MC2 communication

## Overview
This is a cherry-pick of PR #8039 to the v0.18.0 release branch. It restores the `global_bs=0` setting and `mc2_mask` handling for Ascend MC2 operations when all_reduce across DP group cannot be skipped, adding `should_skip_allreduce_across_dp_group()` to `utils.py` with hierarchy constraints. This fixes cross-super-node communication on A3 with `enable_mc2_hierarchy_comm=True` and `HCCL_INTRA_ROCE_ENABLE=1`.

## Technical Significance
The cherry-pick ensures that the critical MC2 communication fix is available in the stable v0.18.0 release for production deployments requiring hierarchical HCCL communication across multi-node Ascend clusters. Without this fix, MoE inference would fail to scale across super-nodes with RoCE interconnects due to incorrect MC2 operator configuration.

## Related
- `technique-pr-vllm-ascend-8039` (Original PR)
- `technique-moe` (MoE MC2 operations)
- `technique-hccl-optimization` (HCCL hierarchical communication)