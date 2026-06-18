---
id: technique-pr-vllm-ascend-6349
title: "PR Insight: vllm-project/vllm-ascend #6349"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - refactor
  - eagle
  - mtp
  - speculative-decoding
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6349"
---

# PR Insight: vllm-project/vllm-ascend #6349

**Title:** [Refactor][EAGLE] 6/N route mtp to eagle except pcp/dcp+mtp

## Overview
This PR refactors speculative decoding by routing MTP (Multi-Token Prediction) functionality to Eagle proposer in most scenarios. Changes include migrating lmhead feature to Eagle, fixing draft_attn_metadatas loss bug, and adding routing logic to use Eagle proposer when PCP and padded drafter batch are not enabled.

## Technical Significance
The refactoring consolidates speculative decoding logic around Eagle proposer while maintaining MTP compatibility for specific scenarios (PCP/dcp+mtp). This reduces code duplication and fixes a critical bug where attention metadata was lost in Eagle mode.

## Related
- `technique-eagle`
- `technique-mtp`
- `technique-speculative-decoding`
- `technique-pcp`