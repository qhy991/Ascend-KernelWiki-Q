---
id: technique-pr-modellink-2337
title: "PR Insight: Ascend/ModelLink #2337"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - moe
  - gradient-fusion
  - communication-overlap
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2337"
---

# PR Insight: Ascend/ModelLink #2337

**Title:** 解决gradient_accumulation_fusion和moe_alltoall_overlap_comm不能同时使能的问题

## Overview
This PR fixes an issue where gradient accumulation fusion and MoE all-to-all communication overlap could not be enabled simultaneously. The fix enables both optimizations to work together for improved MoE training performance.

## Technical Significance
Gradient accumulation fusion reduces communication overhead by combining multiple gradient updates, while MoE all-to-all overlap hides communication latency by overlapping expert routing with computation. Both optimizations are critical for MoE training performance on Ascend hardware. Enabling them together provides additive performance benefits, significantly improving throughput for large MoE models like DeepSeekV3 and Qwen-MoE.

## Related
- `technique-moe-training`
- `technique-alltoall`
- `technique-gradient-accumulation`
- `technique-communication-overlap`