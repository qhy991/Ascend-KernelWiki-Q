---
id: technique-pr-vllm-ascend-2145
title: "PR Insight: vllm-project/vllm-ascend #2145"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - torchair
  - v0-scheduler
  - graph-mode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2145"
---

# PR Insight: vllm-project/vllm-ascend #2145

**Title:** [V1] MTP supports torchair

## Overview
This PR enables MTP (speculative decoding) support with TorchAir graph mode, including V0 Scheduler, single/multi DP, and disaggregated PD scenarios. The implementation modifies `vllm_ascend/worker/mtp_proposer_v1.py`, `vllm_ascend/models/deepseek_mtp.py`, `vllm_ascend/attention/mla_v1.py`, and adds tests. It provides configuration examples for both online serving and offline inference with TorchAir enabled.

## Technical Significance
This integration allows MTP to benefit from TorchAir's graph compilation and execution, reducing host overhead and improving inference performance. Known limitations include no V1 Scheduler support initially (added in PR #2371) and vllm v0.10.0 not supporting metrics with DP > 1. The PR enables efficient MTP execution in graph mode with proper configuration for graph batch sizes and multistream settings.

## Related
- `technique-speculative-decoding`, `technique-torchair-integration`, `technique-aclgraph`, `kernel-mla-v1`