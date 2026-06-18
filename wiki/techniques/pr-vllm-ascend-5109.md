---
id: technique-pr-vllm-ascend-5109
title: "PR Insight: vllm-project/vllm-ascend #5109"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - hccl-optimization
  - all-reduce
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5109"
---

# PR Insight: vllm-project/vllm-ascend #5109

**Title:** fixed fused alltoall execute all reduce

## Overview
This PR fixes an issue where all-reduce was not being executed for the fused alltoall MoE communication path. The fix ensures that when moe_comm_type is FUSED_ALLTOALL and shared_expert_dp_enabled() is false, the shared expert output tensor undergoes all-reduce.

## Technical Significance
Proper all-reduce execution for shared experts in MoE models is critical for numerical correctness and performance on Ascend NPUs. This fix ensures gradient consistency across tensor parallel ranks for MoE computations using the fused alltoall communication pattern.

## Related
- technique-moe
- technique-hccl-optimization
- technique-all-reduce