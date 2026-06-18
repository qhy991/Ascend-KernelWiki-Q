---
id: technique-pr-vllm-ascend-5156
title: "PR Insight: vllm-project/vllm-ascend #5156"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - mc2
  - communication
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5156"
---

# PR Insight: vllm-project/vllm-ascend #5156

**Title:** [bugfix] Use FUSED_MC2 MoE comm path for the op `dispatch_ffn_combine`

## Overview
This PR fixes the MoE communication path by renaming `FUSED_ALLTOALL` to `FUSED_MC2` and updates the implementation to use `FusedMC2CommImpl` with proper token dispatching. The fix ensures correct MoE communication patterns are selected for Ascend A3 with expert parallelism and W8A8 dynamic quantization.

## Technical Significance
The FUSED_MC2 (Fused All-to-All + All-to-All) communication pattern optimizes MoE token routing on Ascend NPUs by fusing multiple communication steps. Proper implementation is critical for MoE performance, reducing communication overhead and improving overall inference throughput.

## Related
- technique-moe
- technique-hccl-optimization
- technique-expert-parallelism