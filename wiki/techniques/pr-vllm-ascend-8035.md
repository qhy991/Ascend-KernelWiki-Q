---
id: technique-pr-vllm-ascend-8035
title: "PR Insight: vllm-project/vllm-ascend #8035"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - eplb
  - scheduling
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8035"
---

# PR Insight: vllm-project/vllm-ascend #8035

**Title:** [EPLB][Feature] Swift balancer policy supports mix placement

## Overview
This PR extends the EPLB Swift balancer policy to support shared expert mix placement for MoE models. The implementation in `vllm_ascend/eplb/core/policy/policy_swift_balancer.py` and related files introduces mixed placement strategies that optimize expert distribution across devices. Performance testing on DeepSeek-V3 shows TTFT improvement from 7824ms to 6698ms and input token throughput increase from 7122 to 8319 token/s.

## Technical Significance
The mixed placement support enables more flexible expert routing strategies for large-scale MoE deployments on Ascend clusters. By allowing experts to be shared across different placement strategies, the Swift balancer can better optimize load balancing while maintaining expert locality for reduced communication overhead. The 14% TTFT improvement and 17% throughput increase demonstrate the effectiveness of the mixed placement policy for optimizing both latency and throughput in multi-device MoE inference.

## Related
- `technique-moe` (MoE expert routing)
- `technique-operator-fusion` (EPLB optimization)
- `pattern-load-balancing` (Expert placement strategies)