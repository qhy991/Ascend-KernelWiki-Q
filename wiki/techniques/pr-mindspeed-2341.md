---
id: technique-pr-mindspeed-2341
title: "PR Insight: Ascend/MindSpeed #2341"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - feature
  - optimizer
  - swap
  - core-r0.12.0
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2341"
---

# PR Insight: Ascend/MindSpeed #2341

**Title:** add swap optimizer to core_r0.12.0

## Overview
This PR adds swap optimizer to core version r0.12.0. Swap optimizer likely involves offloading optimizer states or parameters to CPU memory to reduce GPU/NPU memory usage.

## Technical Significance
Enhances memory optimization capabilities for training larger models by adding swap optimizer support. Swap optimizers are critical for fitting models that exceed device memory capacity.

## Related
- `technique-memory-optimization`
- `technique-swap-optimizer`
- `technique-offloading`