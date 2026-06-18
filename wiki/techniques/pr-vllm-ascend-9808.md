---
id: technique-pr-vllm-ascend-9808
title: "PR Insight: vllm-project/vllm-ascend #9808"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-transfer
  - mooncake
  - hybrid-connector
  - block-ids
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9808"
---

# PR Insight: vllm-project/vllm-ascend #9808

**Title:** [BugFix][P/D] Add compress ratio and block_ids cutting for mooncake hybrid connector

## Overview
This PR adds compress ratio and block_ids cutting capabilities for the Mooncake hybrid connector in prefill/decode scenarios. It optimizes KV transfer efficiency by enabling smarter block selection during hybrid connector operations.

## Technical Significance
Improves KV transfer performance in Mooncake hybrid connector by adding compress ratio tracking and intelligent block_ids cutting. Reduces unnecessary data transfer by only transferring required blocks, improving overall inference efficiency in distributed setups.

## Related
- `technique-kv-cache-paging`, `technique-distributed-kv`, `technique-mooncake`