---
id: technique-pr-vllm-ascend-4947
title: "PR Insight: vllm-project/vllm-ascend #4947"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - routing
  - mtp
  - alltoall
  - dummy-run
  - multi-node
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4947"
---

# PR Insight: vllm-project/vllm-ascend #4947

**Title:** [bugfix] Fix dummy-run and multi-node issues in MoE routing and MTP

## Overview
This PR fixes multiple issues: (1) premature return in moe_init_routing_quant_v2.cpp causing early kernel exit, (2) switching FusedAlltoAllCommImpl to use MC2-based token dispatcher, (3) temporary override in MtpProposer to map FUSED_ALLTOALL back to ALLTOALL for dummy-run flows, and (4) simplifying MoE communication selection for Ascend 910-93 by removing EP-size guard on FUSED_ALLTOALL.

## Technical Significance
Fixes critical bugs in MoE routing that affected multi-node deployments and dummy-run operations. Aligns MoE communication with MC2 algorithm optimized for Ascend devices and enables proper multi-node MoE configurations.

## Related
- `kernel-moe-routing`
- `kernel-fused-alltoall`
- `kernel-mc2`
- `technique-moe-communication`
- `technique-mtp`