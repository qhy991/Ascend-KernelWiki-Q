---
id: technique-pr-mindspeed-2349
title: "PR Insight: Ascend/MindSpeed #2349"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - test
  - cp
  - v2
  - core-r0.12.0
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2349"
---

# PR Insight: Ascend/MindSpeed #2349

**Title:** core_r0.12.0 add cp v2 ut

## Overview
This PR adds unit tests for CP (Context Parallelism) v2 in core version r0.12.0. Context parallelism splits sequences across devices to handle longer contexts.

## Technical Significance
Improves test coverage for context parallelism v2 implementation. CP is important for training models with very long contexts, and proper testing ensures correct sequence splitting and synchronization.

## Related
- `technique-context-parallelism`
- `technique-distributed-training`
- `kernel-attention-ascendc`