---
id: technique-pr-vllm-ascend-7887
title: "PR Insight: vllm-project/vllm-ascend #7887"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - eplb
  - communication
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7887"
---

# PR Insight: vllm-project/vllm-ascend #7887

**Title:** [EPLB][BugFix] Fix moe_load precision in allgather

## Overview
This PR fixes a bug in the EPLB (Expert Parallel Load Balancing) system related to incorrect reshape usage during MoE load operations. The issue caused incorrect tensor layouts after reshape and permute operations. The fix replaces reshape with squeeze for more intuitive and correct tensor manipulation, resulting in improved peak-to-average ratio.

## Technical Significance
MoE load balancing communication patterns are critical for balancing expert load across devices. Incorrect tensor layout handling can lead to precision loss or communication inefficiencies. The fix ensures proper tensor dimension handling during allgather operations, which is essential for maintaining numerical accuracy and communication efficiency in MoE inference.

## Related
- `kernel-moe`
- `technique-hccl-optimization`
- `pattern-moe-load-balancing`