---
id: technique-pr-vllm-ascend-4098
title: "PR Insight: vllm-project/vllm-ascend #4098"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pcp
  - mtp
  - spec-decoding
  - kv-connector
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4098"
---

# PR Insight: vllm-project/vllm-ascend #4098

**Title:** [feature] support pcp + mtp (in pd co-locate scenario)

## Overview
This PR adds support for combining PCP (Prefill Context Parallel) with MTP (Multi-Token Proposal) in PD (Prefill-Decode) co-locate scenarios. The changes include modifications to MLA attention, ACLGraph, llmdatadist connector, MTP proposer, and model runner to enable proper interaction between PCP and MTP optimizations. The PR also includes bug fixes and code cleanup for llmdatadist connector PCP functionality.

## Technical Significance
Combining PCP with MTP enables multiple optimizations simultaneously for PD co-locate deployments, maximizing performance. The interaction between context parallelism and speculative decoding requires careful handling of attention metadata and data paths. This feature enables users to benefit from both PCP's parallelism and MTP's speculative decoding in single deployment.

## Related
- `technique-context-parallel`, `technique-mtp`, `technique-spec-decoding`, `technique-disaggregation`