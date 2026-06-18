---
id: technique-pr-vllm-ascend-7514
title: "PR Insight: vllm-project/vllm-ascend #7514"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pd-disaggregation
  - mooncake
  - kv-transfer
  - error-handling
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7514"
---

# PR Insight: vllm-project/vllm-ascend #7514

**Title:** [P/D] [Bugfix] fix mooncake layerconnector dead when update_decoder_info fail

## Overview
This PR fixes a bug where MoonCake layerwise connector would become dead when update_decoder_info failed in the D node scenario. The fix ensures that node P failures in update_decoder_info don't cause node P to become dead when node D is already dead.

## Technical Significance
This fix matters for robustness in PD (prefill-decode) disaggregation scenarios. The original behavior incorrectly propagated failures, causing the entire system to become dead when a single node failed. The fix ensures proper error handling and isolation, allowing the system to continue operating with available nodes.

## Related
- technique-pd-disaggregation
- technique-kv-transfer