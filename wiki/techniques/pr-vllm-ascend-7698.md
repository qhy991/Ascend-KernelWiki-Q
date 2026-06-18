---
id: technique-pr-vllm-ascend-7698
title: "PR Insight: vllm-project/vllm-ascend #7698"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - hierarchical-communication
  - moe
  - dispatch-v2
  - combine-v2
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7698"
---

# PR Insight: vllm-project/vllm-ascend #7698

**Title:** [feat] support dispatch_v2/combine_v2 hierarchy communication

## Overview
This PR adds support for dispatch_v2/combine_v2 hierarchical communication patterns in MoE token dispatching. It modifies platform configuration, utilities, and MoE token dispatcher to enable hierarchical communication optimization.

## Technical Significance
Enables hierarchical communication optimization for MoE models, reducing communication overhead by organizing communication operations into dispatch_v2 and combine_v2 stages across device hierarchies.

## Related
- `kernel-moe`, `technique-hierarchical-communication`, `pattern-moe-routing`, `technique-token-dispatch`, `hw-hccs`