---
id: technique-pr-vllm-ascend-8908
title: "PR Insight: vllm-project/vllm-ascend #8908"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/8908"
---

# PR Insight: vllm-project/vllm-ascend #8908

**Title:** [BugFix][P/D] Fix Mooncake Connector MTP accuracy bug

## Overview
This PR is a forward-port of the MTP accuracy fix from PR #8890 to the main branch. It fixes the Mooncake Connector accuracy bug when using Multi-Token Prediction (MTP) for speculative decoding by ensuring correct KV cache block mapping between prefill and decode nodes when the prompt length is a multiple of block size. The implementation calculates actual prompt block count and cuts off extra blocks.

## Technical Significance
The forward-port ensures that the critical MTP accuracy fix is available in the development branch for ongoing feature development. The fix maintains correctness for speculative decoding scenarios where prompt lengths align with block boundaries, preventing incorrect token generation or crashes due to KV cache block table mismatches between prefill and decode phases on Ascend NPUs.

## Related
- `technique-pr-vllm-ascend-8890` (Original v0.18.0 fix)
- `technique-speculative-decoding` (MTP speculative decoding)
- `pattern-kv-cache` (KV cache block management)