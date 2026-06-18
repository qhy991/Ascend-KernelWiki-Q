---
id: technique-pr-vllm-ascend-2444
title: "PR Insight: vllm-project/vllm-ascend #2444"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - disaggregated-prefill
  - v1-scheduler
  - v0.9.1
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2444"
---

# PR Insight: vllm-project/vllm-ascend #2444

**Title:** [0.9.1] [BUGFIX] support mtp in disaggregated-prefill scenario

## Overview
This PR adds MTP support for disaggregated-prefill scenarios, enabling speculative decoding in the P-D (prefill-decode) disaggregated architecture. The implementation modifies `vllm_ascend/attention/mla_v1.py`, `vllm_ascend/worker/model_runner_v1.py`, and `vllm_ascend/worker/worker_v1.py`.

## Technical Significance
This feature enables MTP to work in disaggregated inference setups where prefill and decode are handled by separate node types. The fix ensures proper interaction between MTP's speculative decoding and the disaggregated architecture's KV transfer and scheduling mechanisms.

## Related
- `technique-speculative-decoding`, `technique-disaggregated-inference`, `kernel-mla-v1`, `technique-kv-cache-transfer`