---
id: technique-pr-mindspeed-1083
title: "PR Insight: Ascend/MindSpeed #1083"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - ring-attention
  - bugfix
  - performance
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1083"
---

# PR Insight: Ascend/MindSpeed #1083

**Title:** fix: npu_ring_attention_update when actual_seq_qlen is none; perf: tests

## Overview
This PR fixes the `npu_ring_attention_update` function when `actual_seq_qlen` is None, and includes performance improvements for tests. Ring attention is a technique for processing long sequences across multiple devices.

## Technical Significance
Ring attention is critical for training models with very long sequences on Ascend clusters. This fix ensures correct handling of edge cases in sequence length handling, while performance improvements in tests enable faster validation and iteration during development.

## Related
- kernel-attention
- technique-communication-optimization