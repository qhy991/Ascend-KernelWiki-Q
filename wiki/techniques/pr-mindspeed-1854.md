---
id: technique-pr-mindspeed-1854
title: "PR Insight: Ascend/MindSpeed #1854"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - ulysses
  - kv-cache
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1854"
---

# PR Insight: Ascend/MindSpeed #1854

**Title:** 修复Ulysses KV缓存引入的bug

## Overview
This PR fixes a bug introduced by Ulysses KV caching functionality. The issue likely affects the correctness or performance of attention computation when using sequence parallelism with KV cache.

## Technical Significance
KV caching is essential for efficient autoregressive inference. Fixing bugs in Ulysses KV caching ensures correct attention computation and prevents data corruption or performance degradation in sequence parallel workloads on Ascend NPUs.

## Related
- kv-cache management
- sequence-parallel patterns
- attention-optimization