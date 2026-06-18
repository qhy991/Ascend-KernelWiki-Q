---
id: technique-pr-mindspeed-2431
title: "PR Insight: Ascend/MindSpeed #2431"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - feature
  - zero-memory
  - memory-optimization
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2431"
---

# PR Insight: Ascend/MindSpeed #2431

**Title:** 【feat】Zero_Memory update.

## Overview
This PR updates the Zero_Memory feature, which is likely related to ZeRO (Zero Redundancy Optimizer) memory optimization techniques. ZeRO reduces memory usage by partitioning optimizer states, gradients, and parameters across devices.

## Technical Significance
Enhances memory optimization capabilities for training large models on Ascend NPUs. ZeRO techniques are critical for fitting larger models into limited device memory by eliminating redundant parameter copies.

## Related
- `technique-memory-optimization`
- `technique-distributed-training`
- `technique-zero-redundancy`