---
id: technique-pr-vllm-ascend-6155
title: "PR Insight: vllm-project/vllm-ascend #6155"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mooncake
  - pd-colocation
  - logging
  - zmq
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6155"
---

# PR Insight: vllm-project/vllm-ascend #6155

**Title:** [P/D] Mooncake connector add zmq socket fail log

## Overview
This PR adds error logging for ZMQ socket failures in the Mooncake connector for P/D (Prefill/Decode) colocation scenarios. The changes improve debugging by logging socket connection failures in the KV transfer P2P Mooncake connector.

## Technical Significance
Mooncake uses ZMQ (ZeroMQ) for inter-process communication between prefill and decode nodes in disaggregated inference. Adding failure logs for ZMQ socket operations helps diagnose network issues, resource exhaustion, or configuration problems in distributed KV transfer setups, improving operational observability and debugging efficiency.

## Related
- `technique-pd-colocation`, `technique-mooncake`, `technique-kv-transfer`