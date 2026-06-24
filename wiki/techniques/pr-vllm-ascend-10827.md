---
id: technique-dsa-cp-index-cache
title: "Context-Parallel Aware Index Caching for DeepSeek Attention"
type: wiki-technique
confidence: verified
architectures:
  - ascend910b
kernel_types:
  - attention
tags:
  - dsa-cp
sources:
  - pr-vllm-ascend-10827
---

# Context-Parallel Aware Index Caching for DeepSeek Attention

## Overview
Context Parallelism (CP) partitions the sequence dimension across multiple devices. When deploying Context-Parallel DeepSeek Attention (DSA-CP), local index caches for Top-K routing must understand the global context.

## The Issue
Using standard `num_input_token` calculations for Top-K index caches will result in out-of-bounds or misaligned indices because a single device only sees a slice of the sequence. The index cache must fetch `num_input_token` directly from the globally synchronized DSA-CP context state, not the local batch context.
