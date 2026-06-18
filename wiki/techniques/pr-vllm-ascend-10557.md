---
id: technique-pr-vllm-ascend-10557
title: "PR Insight: vllm-project/vllm-ascend #10557"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - moe
  - communication
  - graph-mode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10557"
---

# PR Insight: vllm-project/vllm-ascend #10557

**Title:** [Ascend950] [BugFix]Fix the issue where MOE model output is garbled when communicating with allgather while SP is disabled

## Overview
This PR fixes a garbled output issue for MoE models when using the ALLGATHER communication path without sequence parallelism enabled on Ascend 950. In non-SP MoE scenarios, the final MoE output still needs to be reduced across TP/EP ranks. However, when running in graph mode, the communication decision may be specialized during graph compilation, especially when switching between different MoE communication paths like MC2 and ALLGATHER. This can cause the required final all-reduce for the ALLGATHER path to be skipped, leading to incorrect MoE output and garbled model responses.

## Technical Significance
This is a critical graph mode correctness fix for MoE inference. The issue demonstrates the complexity of maintaining correct communication semantics when using graph mode, where specialized compilation can eliminate required communication operations. The fix moves the final MoE output reduction decision into the graph/runtime path, ensuring the correct reduce behavior is preserved for non-sequence-parallel configurations. This is essential for MoE models to produce correct results when ALLGATHER is selected while SP is disabled.

## Related
- `technique-moe`
- `technique-graph-mode`
- `technique-allgather`