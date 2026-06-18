---
id: technique-pr-sgl-kernel-npu-290
title: "PR Insight: sgl-project/sgl-kernel-npu #290"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qkv
  - rmsnorm
  - rope
  - bugfix
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/290"
---

# PR Insight: sgl-project/sgl-kernel-npu #290

**Title:** split_qkv_rmsnorm_rope bugfix

## Overview
Fixes bugs in the split_qkv_rmsnorm_rope operation and adds comprehensive tests. The fix addresses issues discovered after the previous modification to make normalization optional.

## Technical Significance
Bug fixes in core QKV processing operations are critical for maintaining model accuracy and stability. The addition of comprehensive tests ensures that future changes don't introduce regressions, providing confidence in the correctness of QKV splitting, RMS normalization, and RoPE operations.

## Related
- `wiki-technique-qkv-splitting`
- `wiki-technique-rmsnorm`
- `wiki-technique-rope`
- `wiki-technique-bugfix`