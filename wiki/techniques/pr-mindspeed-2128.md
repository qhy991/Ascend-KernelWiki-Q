---
id: technique-pr-mindspeed-2128
title: "PR Insight: Ascend/MindSpeed #2128"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - moe
  - bugfix
  - performance
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2128"
---

# PR Insight: Ascend/MindSpeed #2128

**Title:** 【Fix】Create global stream for SequentialMLP

## Overview
This PR fixes an issue by creating a global execution stream for SequentialMLP in MoE (Mixture of Experts) training. The fix addresses potential synchronization and performance issues in expert computation.

## Technical Significance
Global stream management is critical for efficient kernel execution and synchronization on Ascend NPUs. The fix ensures that SequentialMLP operations are properly scheduled and synchronized, avoiding race conditions or inefficient execution ordering. This optimization is particularly important for MoE models where expert computations must be correctly coordinated with token routing and dispatch operations. Proper stream management improves performance by enabling better overlap between computation and communication.

## Related
- `technique-event-sync`
- `technique-cube-vector-overlap`