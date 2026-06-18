---
id: technique-pr-sgl-kernel-npu-61
title: "PR Insight: sgl-project/sgl-kernel-npu #61"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - notify-dispatch
  - synchronization
  - bugfix
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/61"
---

# PR Insight: sgl-project/sgl-kernel-npu #61

**Title:** fix hostbound before notify dispatch

## Overview
This PR fixes synchronization issues by adding proper hostbound synchronization before notify dispatch operations. Updates notify dispatch kernel implementation (96 lines) and tiling logic to ensure correct execution order.

## Technical Significance
Resolves race conditions that could cause incorrect dispatch behavior due to asynchronous execution. Proper hostbound synchronization ensures all preceding operations complete before notify dispatch begins, critical for correct MoE expert routing coordination in distributed inference.

## Related
- technique-event-sync
- technique-dispatch-synchronization
- technique-host-synchronization