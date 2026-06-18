---
id: technique-pr-vllm-ascend-9810
title: "PR Insight: vllm-project/vllm-ascend #9810"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/9810"
---

# PR Insight: vllm-project/vllm-ascend #9810

**Title:** [0.20.2][BugFix][P/D] Add compress ratio and block_ids cutting for mooncake hybrid connector

## Overview
This PR is a backport of the Mooncake hybrid connector improvements (#9808) to v0.20.2, adding compress ratio and block_ids cutting capabilities for improved KV transfer efficiency.

## Technical Significance
Ensures production stability by backporting critical KV transfer optimizations to the v0.20.2 release. Enables efficient block selection and compression in Mooncake hybrid connector for production deployments.

## Related
- `technique-kv-cache-paging`, `technique-distributed-kv`, `technique-mooncake`