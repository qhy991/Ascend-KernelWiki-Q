---
id: technique-pr-vllm-ascend-5521
title: "PR Insight: vllm-project/vllm-ascend #5521"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - eplb
  - bugfix
  - dispatch
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5521"
---

# PR Insight: vllm-project/vllm-ascend #5521

**Title:** [smoke][bugfix] moe_init_routing_v2 active_expert_range use int type

## Overview
This PR fixes a type mismatch bug in the MOE_init_routing_v2 dispatch allgather operation where the active_expert_range parameter was incorrectly converted to tensor type instead of integer type. The issue was introduced by PR #5311 when unifying variable usage for local_num_experts.

## Technical Significance
Correct type handling in MoE dispatch operations is critical for NPU kernel compatibility. The fix ensures that the MoE routing kernel receives the expected integer format for active_expert_range, preventing runtime errors and maintaining accuracy in large-scale MoE inference with expert parallelism.

## Related
- `pattern-moe` (MoE patterns and operations)
- `technique-expert-parallelism` (Expert parallel dispatch)
- `kernel-moe` (MoE routing operations)