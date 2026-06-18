---
id: technique-pr-mindspeed-2355
title: "PR Insight: Ascend/MindSpeed #2355"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - recompute
  - core-r0.12.1
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2355"
---

# PR Insight: Ascend/MindSpeed #2355

**Title:** recompute fix for core_r0.12.1

## Overview
This PR fixes recompute functionality for core version r0.12.1. Recompute is a memory optimization technique that trades computation for memory by recomputing activations during backward pass.

## Technical Significance
Ensures recompute works correctly in the r0.12.1 core version, enabling training of larger models by reducing memory usage. Proper recompute implementation is critical for memory-constrained training scenarios.

## Related
- `technique-recompute`
- `technique-memory-optimization`