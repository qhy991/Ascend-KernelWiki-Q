---
id: technique-pr-mindspeed-2424
title: "PR Insight: Ascend/MindSpeed #2424"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - test
  - recompute
  - fp32
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2424"
---

# PR Insight: Ascend/MindSpeed #2424

**Title:** test:  add ut for recompute and reuse_fp32_param

## Overview
This PR adds unit tests for recompute functionality and the reuse_fp32_param feature. Recompute is a memory optimization technique that trades computation for memory by recomputing activations during backward pass.

## Technical Significance
Ensures correctness of memory optimization features. Recompute reduces memory usage during training, and reuse_fp32_param likely relates to maintaining precision for parameters. Proper test coverage prevents regressions in these critical training optimizations.

## Related
- `technique-recompute`
- `technique-memory-optimization`