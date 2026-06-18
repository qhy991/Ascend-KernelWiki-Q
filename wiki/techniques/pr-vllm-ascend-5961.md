---
id: technique-pr-vllm-ascend-5961
title: "PR Insight: vllm-project/vllm-ascend #5961"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mooncake
  - pd-disaggregation
  - kv-cache
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5961"
---

# PR Insight: vllm-project/vllm-ascend #5961

**Title:** [0.13.0][bugfix] fix mooncake kv cache transfer when one P has multi nodes

## Overview
This is a cherry-pick of PR #5960 for the v0.13.0 release branch. It fixes the same Mooncake KV cache transfer issue when a Prefill node has multiple physical nodes by providing P node IPs to D nodes through the remote_port_send_num parameter.

## Technical Significance
This fix ensures the v0.13.0 branch maintains robustness for PD disaggregation with multi-node P deployments. The cherry-pick applies the same IP routing fix to the mooncake_connector module, preventing transfer errors when D nodes need to send release messages to multi-node P deployments.

## Related
- `technique-pr-vllm-ascend-5960`, `technique-mooncake`, `technique-pd-disaggregation`