---
id: technique-pr-vllm-ascend-5388
title: "PR Insight: vllm-project/vllm-ascend #5388"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - ep
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5388"
---

# PR Insight: vllm-project/vllm-ascend #5388

**Title:** [Bugfix] Fix unsuitable moe_comm_type under ep=1 scenario

## Overview
This PR fixes an issue where `moe_comm_type` was not chosen correctly when `ep=1` (expert parallelism size of 1). The fix ensures proper communication method selection even in single-rank expert parallelism scenarios.

## Technical Significance
Even when EP=1, proper MoE communication method selection is critical for correctness. Machine-dependent differences could cause errors with inappropriate communication types. This fix ensures robust MoE operation across different deployment configurations on Ascend NPUs.

## Related
- technique-moe
- technique-expert-parallelism
- technique-communication-methods