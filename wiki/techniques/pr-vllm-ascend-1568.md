---
id: technique-pr-vllm-ascend-1568
title: "PR Insight: vllm-project/vllm-ascend #1568"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mooncake
  - distributed
  - connector
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1568"
---

# PR Insight: vllm-project/vllm-ascend #1568

**Title:** [P/D] Mooncake Connector for v1 distributed

## Overview
This PR adds Moonake connector support for V1 distributed inference, enabling integration with Mooncake's distributed serving infrastructure.

## Technical Significance
Enables vLLM Ascend V1 to participate in Mooncake's distributed serving ecosystem by providing KV cache and state synchronization connectors. The implementation includes deployment documentation and comprehensive test coverage for Mooncake integration scenarios.

## Related
- `technique-disaggregated-prefill`
- `technique-kv-cache-paging`
- `technique-mooncake`