---
id: technique-pr-mindspeed-1979
title: "PR Insight: Ascend/MindSpeed #1979"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - attention
  - ulysses
  - kv-cache
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1979"
---

# PR Insight: Ascend/MindSpeed #1979

**Title:** feat: unaligned Ulysses, currently does not support KV caching

## Overview
This PR implements unaligned Ulysses sequence parallelism for attention mechanisms. The feature currently does not support KV caching, indicating it's focused on inference or training scenarios without KV reuse.

## Technical Significance
Unaligned Ulysses enables sequence parallelism for attention without requiring sequence length to be divisible by the degree of parallelism. This is important for handling variable-length sequences in real-world workloads, though the lack of KV caching support limits its use in autoregressive inference.

## Related
- flash-attention
- sequence-parallel patterns
- attention-optimization