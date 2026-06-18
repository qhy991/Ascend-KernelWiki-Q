---
id: technique-pr-vllm-ascend-5960
title: "PR Insight: vllm-project/vllm-ascend #5960"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mooncake
  - pd-disaggregation
  - kv-cache
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5960"
---

# PR Insight: vllm-project/vllm-ascend #5960

**Title:** [main][bugfix] fix mooncake kv cache transfer when one P has multi nodes

## Overview
This PR fixes Mooncake KV cache transfer failures in PD disaggregation when a Prefill node has multiple physical nodes. The issue occurs when D nodes need to send release messages to P nodes but don't know the correct IP addresses for multi-node P deployments.

## Technical Significance
In PD disaggregation, if a P rank doesn't need to transfer KV cache to any D rank, the D node should send a release message to the P node. With multi-node P deployments, D nodes need to know the corresponding IP in each P node to send messages correctly. The fix provides P node IPs to D nodes through the remote_port_send_num parameter, ensuring proper message routing and preventing transfer errors.

## Related
- `technique-mooncake`, `technique-pd-disaggregation`, `technique-kv-cache-transfer`