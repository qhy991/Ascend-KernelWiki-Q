---
id: technique-pr-vllm-ascend-5822
title: "PR Insight: vllm-project/vllm-ascend #5822"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mooncake
  - pd-disaggregation
  - elastic-scaling
  - kv-cache
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5822"
---

# PR Insight: vllm-project/vllm-ascend #5822

**Title:** [Feature] Mooncake connector get remote ptp size

## Overview
This PR enables elastic scaling support for the Mooncake connector in PD (Prefill-Decode) disaggregation scenarios. The prefill node's tensor parallel size is now transferred through the request's `kv_transfer_params`, allowing decode nodes to retrieve it directly instead of relying on static connector configuration.

## Technical Significance
Elastic scaling requires dynamic tensor parallel sizes across nodes. Previously, the Mooncake connector assumed fixed TP sizes, limiting scaling flexibility. By propagating the prefill node's TP size through request parameters, decode nodes can correctly handle KV cache transfers from prefill nodes with different TP configurations. This enables heterogeneous deployments where prefill and decode nodes can have different parallel configurations, improving resource utilization and scaling flexibility.

## Related
- `technique-pd-disaggregation`, `technique-kv-cache-transfer`, `technique-mooncake`