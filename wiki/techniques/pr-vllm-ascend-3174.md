---
id: technique-pr-vllm-ascend-3174
title: "PR Insight: vllm-project/vllm-ascend #3174"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - spec-decoding
  - batch-reordering
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3174"
---

# PR Insight: vllm-project/vllm-ascend #3174

**Title:** bugfix for mtp>1

## Overview
This PR fixes bugs when MTP (Multi-Token Proposal) count exceeds 1 and reorders the input batch when MTP proposals are not accepted. The fixes ensure correct behavior for multi-token speculative decoding scenarios.

## Technical Significance
Multi-token speculative decoding improves acceptance rates but adds complexity to batch management. Proper batch reordering when proposals are rejected ensures correct execution order and prevents corruption. This enables effective use of multi-token proposals to accelerate inference.

## Related
- `technique-spec-decoding`, `kernel-mtp-ascendc`, `pattern-batch-management`