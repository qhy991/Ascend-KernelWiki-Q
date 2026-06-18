---
id: technique-pr-vllm-ascend-2509
title: "PR Insight: vllm-project/vllm-ascend #2509"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - fia
  - disaggregated-inference
  - v0.9.1
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2509"
---

# PR Insight: vllm-project/vllm-ascend #2509

**Title:** [0.9.1][BUGFIX] FIX FIA input when mtp is enabled in pd Disaggregation scenario

## Overview
This PR fixes a bug in the P-D disaggregated scenario where MTP is enabled, triggered when receiving over 16 requests from the prefill node for one decode node. The issue is that `torch_npu.npu_fused_infer_attention_score` can only accept 16 sequence lengths for query in one batch. The fix modifies `vllm_ascend/attention/mla_v1.py`.

## Technical Significance
This bugfix ensures correct FIA (Fused Infer Attention) input handling when MTP is used in disaggregated inference, preventing errors when the batch size exceeds the attention kernel's limitations. The fix is particularly important for high-load scenarios with many concurrent requests.

## Related
- `technique-speculative-decoding`, `technique-disaggregated-inference`, `kernel-mla-v1`, `kernel-fia`