---
id: technique-pr-vllm-ascend-3256
title: "PR Insight: vllm-project/vllm-ascend #3256"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - hccl-optimization
  - decode
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3256"
---

# PR Insight: vllm-project/vllm-ascend #3256

**Title:** [Core]Append padding logic for Attention

## Overview
This PR aims to add padding logic to seq_lens、block_tables when running in full decode scenario. Before this PR, the number of input tokens with padding might exceeds corresponding seq_lens. For example, when running in full decode scenario:

## Technical Significance
Implements padding logic for attention mechanisms (including MLA and SFA) to handle variable-length sequences efficiently in batched inference scenarios.

## Related
- `hw-cube-unit`
