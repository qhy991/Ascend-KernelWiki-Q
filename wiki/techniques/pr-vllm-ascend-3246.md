---
id: technique-pr-vllm-ascend-3246
title: "PR Insight: vllm-project/vllm-ascend #3246"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - hccl-optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3246"
---

# PR Insight: vllm-project/vllm-ascend #3246

**Title:** [Quickfix] Fix dp+ep+tp error when sp chunked the hidden_states

## Overview
Fix dp+ep+tp inplace copy error when sp chunked the `hidden_states`.

## Technical Significance
Fixes distributed parallelism errors when combining data, expert, and tensor parallelism with sequence parallelism that chunks hidden states, ensuring correct tensor operations.

## Related
- `technique-moe-routing`
- `technique-hccl-optimization`
