---
id: technique-pr-vllm-ascend-8890
title: "PR Insight: vllm-project/vllm-ascend #8890"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - speculative-decoding
  - kv-cache
  - mtp
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8890"
---

# PR Insight: vllm-project/vllm-ascend #8890

**Title:** [v0.18.0][Bugfix][P/D] Fix Mooncake Connector MTP accuracy bug

## Overview
This PR fixes an accuracy bug in the Mooncake Connector when using Multi-Token Prediction (MTP) for speculative decoding. The issue occurred because the prefill node allocates extra KV cache blocks used by MTP, while the decode node does not allocate blocks when waiting for KV transfer. When the prompt length is a multiple of the block size, the blocks of P and D may not be in one-to-one correspondence. The fix calculates the number of blocks occupied by the actual prompt and cuts off extra blocks.

## Technical Significance
The bug caused incorrect KV cache mapping between prefill and decode nodes in speculative decoding scenarios, particularly for prompt lengths aligned to block size boundaries. This could lead to wrong token generation or crashes. The fix ensures correct block table synchronization between prefill and decode phases by accurately accounting for the actual prompt length, maintaining correctness for MTP-based speculative decoding on Ascend NPUs.

## Related
- `technique-speculative-decoding` (MTP speculative decoding)
- `pattern-kv-cache` (KV cache block management)
- `pattern-prefill-decode-synchronization` (P/D coordination)