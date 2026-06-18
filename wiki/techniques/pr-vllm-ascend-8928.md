---
id: technique-pr-vllm-ascend-8928
title: "PR Insight: vllm-project/vllm-ascend #8928"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - speculative-decoding
  - multi-token-prediction
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8928"
---

# PR Insight: vllm-project/vllm-ascend #8928

**Title:** [BugFix] Fix mooncake_connector's incompatibility with multi-layer draft model

## Overview
This PR fixes an incompatibility issue in the mooncake_connector when working with multi-layer draft models during speculative decoding. The connector previously assumed only one additional layer for MTP (Multi-Token Prediction) but didn't properly handle draft models with multiple hidden layers. The implementation updates `vllm_ascend/distributed/kv_transfer/kv_p2p/mooncake_connector.py` to correctly support multi-layer draft architectures.

## Technical Significance
Multi-layer draft models are increasingly used in speculative decoding to improve acceptance rates and overall throughput. The bug limited the mooncake_connector to single-layer drafts, preventing optimization gains from advanced draft architectures. The fix enables proper KV transfer and coordination for multi-layer draft models, improving speculative decoding effectiveness on Ascend NPUs by supporting more sophisticated draft model architectures.

## Related
- `technique-speculative-decoding` (Multi-layer MTP)
- `pattern-draft-models` (Draft model architectures)
- `pattern-kv-transfer` (KV cache transfer)