---
id: technique-pr-sgl-kernel-npu-428
title: "PR Insight: sgl-project/sgl-kernel-npu #428"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - causal-conv1d
  - state-update
  - mamba
  - bugfix
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/428"
---

# PR Insight: sgl-project/sgl-kernel-npu #428

**Title:** Fix conv1d update state shift

## Overview
This PR fixes a state shift bug in the causal_conv1d_update kernel where state indices were not properly computed, leading to incorrect state management during Mamba-style attention updates. The modification corrects the host-side and kernel-side logic for proper state position calculation.

## Technical Significance
Correct state management is critical for recurrent attention mechanisms where state must be accurately maintained and updated across processing steps. The fix ensures proper state propagation in Mamba models, preventing accuracy degradation from misaligned state indices.

## Related
- `kernel-causal-conv1d`, `kernel-mamba`, `kernel-state-update`, `technique-bugfix`