---
id: technique-pr-vllm-ascend-5552
title: "PR Insight: vllm-project/vllm-ascend #5552"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - eplb
  - dispatch
  - aclnn
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5552"
---

# PR Insight: vllm-project/vllm-ascend #5552

**Title:** [Feature]EPLB:Adapt DispatchGmmCombineDecode operator to eplb tensor list and expert token numbers

## Overview
This PR adapts the DispatchGmmCombineDecode operator to support EPLB tensor lists and expert token counting. The operator now supports gmm1, gmm2, gmm1Scale, and gmm2Scale formats as lists and counts how many tokens each local expert receives via the expertTokensNum parameter, enabling better load balancing.

## Technical Significance
The enhanced DispatchGmmCombineDecode operator provides more granular control over expert distribution in EPLB scenarios, allowing for better resource utilization and load balancing. The tensor list support enables flexible weight scale handling while expert token counting provides visibility into load distribution across experts.

## Related
- `pattern-moe` (MoE patterns and operations)
- `technique-expert-parallelism` (Expert parallel load balancing)
- `kernel-moe` (MoE dispatch operations)
- `technique-aclnn` (Custom operator development)