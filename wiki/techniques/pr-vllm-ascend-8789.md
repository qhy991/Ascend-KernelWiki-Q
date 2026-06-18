---
id: technique-pr-vllm-ascend-8789
title: "PR Insight: vllm-project/vllm-ascend #8789"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - ffn
  - xmask
  - bugfix
  - ascendc
  - operator
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8789"
---

# PR Insight: vllm-project/vllm-ascend #8789

**Title:** [BugFix]xmask feature for dispatch_ffn_combine operator

## Overview
This PR fixes a memory alignment issue in the `ApplyXActiveMask` function within the `dispatch_ffn_combine` operator kernel. The unaligned data movement address was causing some tokens to be masked incorrectly. The fix ensures proper memory access alignment and correct mask application behavior in the C++ kernel implementation.

## Technical Significance
The `dispatch_ffn_combine` operator is a custom AscendC kernel that combines FFN (Feed-Forward Network) dispatch operations. XActiveMask is a feature that applies selective activation masking to improve efficiency or implement sparsity. Memory alignment issues can cause silent data corruption where incorrect tokens are masked, leading to accuracy degradation. Proper alignment is particularly important for NPU memory access patterns and vectorized operations.

## Related
- `kernel-matmul-ascendc`
- `technique-operator-fusion`
- `hw-vector-unit`