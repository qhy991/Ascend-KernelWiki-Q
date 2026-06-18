---
id: technique-pr-vllm-ascend-8039
title: "PR Insight: vllm-project/vllm-ascend #8039"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/8039"
---

# PR Insight: vllm-project/vllm-ascend #8039

**Title:** [BugFix] Restore global_bs=0 and mc2_mask for uniform-token dispatching and support inter-node roce hierarchical MC2 communication

## Overview
This PR restores the `global_bs=0` setting and `mc2_mask` handling for Ascend MC2 operations when all_reduce across DP group cannot be skipped. The implementation adds `should_skip_allreduce_across_dp_group()` to `utils.py` with hierarchy constraints, sets `global_bs=0` when allreduce is not skipped, and adds `mc2_mask` field to `MoEMC2CombineMetadata` for dispatch→combine propagation. This fixes cross-super-node communication on A3 with `enable_mc2_hierarchy_comm=True` and `HCCL_INTRA_ROCE_ENABLE=1`.

## Technical Significance
The bug broke inter-node hierarchical MC2 communication because PR #4983 always passed non-zero `global_bs` without `mc2_mask`, which is incompatible with Ascend MC2 operators requiring `global_bs=0` + `mc2_mask` for hierarchical communication. The fix ensures proper MC2 operator configuration for uniform-token dispatching across hierarchical HCCL communication domains, enabling correct MoE expert communication across multi-node Ascend clusters with RoCE interconnects.

## Related
- `technique-moe` (MoE MC2 operations)
- `technique-hccl-optimization` (HCCL hierarchical communication)
- `pattern-multi-node` (Inter-node synchronization)