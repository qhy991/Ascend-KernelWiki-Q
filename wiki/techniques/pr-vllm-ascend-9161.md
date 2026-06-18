---
id: technique-pr-vllm-ascend-9161
title: "PR Insight: vllm-project/vllm-ascend #9161"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mooncake
  - kv-transfer
  - qwen3.5
  - distributed
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9161"
---

# PR Insight: vllm-project/vllm-ascend #9161

**Title:** [v0.18.0][Feature][P/D] Mooncake Connector v1 add support for qwen3.5

## Overview
This PR adds Qwen3.5 series model support to the Mooncake Connector v1 for distributed KV transfer. The implementation in `vllm_ascend/distributed/kv_transfer/kv_p2p/mooncake_connector.py` enables disaggregated inference scenarios where prefill and decode stages run on separate devices with efficient KV cache transfer.

## Technical Significance
The Mooncake Connector enables distributed inference by decoupling prefill and decode execution across multiple devices, improving resource utilization and scaling for large models. Qwen3.5 support extends this capability to one of the most widely used Chinese language model families, enabling efficient distributed inference deployments with proper KV cache transfer between prefill and decode stages.

## Related
- `technique-kv-cache-paging`, `technique-hccl-optimization`, `kernel-attention-ascendc`