---
id: technique-pr-vllm-ascend-5787
title: "PR Insight: vllm-project/vllm-ascend #5787"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - dispatch-ffn-combine
  - ep32
  - configuration
  - moe
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5787"
---

# PR Insight: vllm-project/vllm-ascend #5787

**Title:** enable ep32 for dispatch_ffn_combine

## Overview
This PR enables ep32 (expert parallel with 32 experts per device) support for the dispatch_ffn_combine operator. The implementation updates configuration settings in `ascend_forward_context.py` and `envs.py` to allow the operator to work with ep32 configurations. This enables the use of dispatch_ffn_combine in scenarios with higher expert parallelism degrees.

## Technical Significance
This configuration change enables support for more aggressive expert parallelism by allowing the dispatch_ffn_combine operator to work with ep32 configurations. For large MoE models that can benefit from distributing experts across more devices, this enables better scaling and resource utilization. The single operator testing confirmed the functionality, allowing users to leverage higher expert parallel degrees for improved throughput on large MoE deployments.

## Related
- `technique-moe`, `technique-expert-parallel`, `technique-dispatch-ffn-combine`