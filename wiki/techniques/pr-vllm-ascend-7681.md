---
id: technique-pr-vllm-ascend-7681
title: "PR Insight: vllm-project/vllm-ascend #7681"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - context-parallel
  - deepseek-v3
  - mla
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7681"
---

# PR Insight: vllm-project/vllm-ascend #7681

**Title:** [v0.18.0][Bugfix] fix ds3.2 dcp mtp

## Overview
This PR fixes issues with DeepSeek V3.2 distributed context parallel (DCP) and multi-token prediction (MTP). The fix affects attention V1, context parallel attention, MLA v1, SFA v1, and speculative decoding components.

## Technical Significance
Resolves correctness issues in DeepSeek V3.2 inference with distributed context parallelism, ensuring accurate MTP and attention computation across multiple devices.

## Related
- `kernel-mla`, `kernel-attention`, `technique-context-parallel`, `pattern-deepseek-architecture`, `technique-speculative-decoding`