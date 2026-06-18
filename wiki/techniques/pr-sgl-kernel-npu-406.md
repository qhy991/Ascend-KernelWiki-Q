---
id: technique-pr-sgl-kernel-npu-406
title: "PR Insight: sgl-project/sgl-kernel-npu #406"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - causal-conv1d
  - mamba
  - bugfix
  - bounds-checking
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/406"
---

# PR Insight: sgl-project/sgl-kernel-npu #406

**Title:** fix(mamba): clamp negative gather indices in causal_conv1d final_states

## Overview
This PR fixes a crash in causal_conv1d_fn during decode when has_initial_state=False and seqlen < width-1, which caused negative gather indices leading to NPU hardware out-of-bounds errors. The fix clamps indices to [0, x.size(2)-1] and zero-fills out-of-bounds positions, maintaining semantic equivalence to the original F.pad behavior.

## Technical Significance
The bounds checking fix prevents hardware-level memory access violations in NPU gather operations, which are more severe than Python exceptions. This ensures robust operation during decode phases where sequence length varies, particularly important for models like Qwen3.5 that use batched causal_conv1d with dynamic sequence lengths.

## Related
- `kernel-causal-conv1d`, `kernel-mamba`, `technique-bugfix`, `technique-bounds-checking`