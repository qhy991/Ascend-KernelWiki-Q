---
id: technique-pr-vllm-ascend-2371
title: "PR Insight: vllm-project/vllm-ascend #2371"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - v1-scheduler
  - attn-metadata
  - v0.9.1
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2371"
---

# PR Insight: vllm-project/vllm-ascend #2371

**Title:** [v0.9.1] MTP supports V1 scheduler

## Overview
This PR adds V1 scheduler support for MTP (speculative decoding) and refactors attention metadata building. The implementation modifies `vllm_ascend/attention/attention_v1.py`, `vllm_ascend/attention/mla_v1.py`, `vllm_ascend/attention/utils.py`, `vllm_ascend/worker/model_runner_v1.py`, and `vllm_ascend/worker/mtp_proposer_v1.py`.

## Technical Significance
This feature enables MTP to work with V1 scheduler (chunked prefill), which is important for improved prefill throughput. The refactored attention metadata building improves code organization and makes it easier to maintain and extend. Testing covered v0.9.1-dev with various configurations including TP16, DP4-TP4, and 1P1D setups.

## Related
- `technique-speculative-decoding`, `kernel-mla-v1`, `kernel-attention-v1`, `technique-chunked-prefill`