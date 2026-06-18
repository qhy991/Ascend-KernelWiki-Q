---
id: technique-pr-vllm-ascend-6402
title: "PR Insight: vllm-project/vllm-ascend #6402"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kernel
  - dispatch
  - moe
  - token-counting
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6402"
---

# PR Insight: vllm-project/vllm-ascend #6402

**Title:** [Refactor] Add expert processed token count output for DispatchFFNCombine/DispatchFFNCombineBF16

## Overview
This PR adds a new output tensor `expert_token_nums` to both DispatchFFNCombine and DispatchFFNCombineBF16 operators to track token distribution among experts. The output is a 1D int32 tensor with shape (local_expert_num,) representing the number of tokens processed by each expert on the current card.

## Technical Significance
Token counting output enables better load balancing monitoring and debugging for MoE inference. The data helps identify expert utilization patterns and can be used for dynamic routing optimization or performance analysis.

## Related
- `technique-dispatch`
- `technique-moe`
- `technique-token-counting`
- `technique-load-balancing`