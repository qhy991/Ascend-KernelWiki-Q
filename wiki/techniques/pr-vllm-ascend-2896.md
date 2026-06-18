---
id: technique-pr-vllm-ascend-2896
title: "PR Insight: vllm-project/vllm-ascend #2896"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - nz-format
  - quantization
  - linear
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2896"
---

# PR Insight: vllm-project/vllm-ascend #2896

**Title:** Revert "[Feat] Unquantized linear nz support (#2619)"

## Overview
This PR reverts the unquantized linear NZ format support feature (PR #2619) due to issues reported in issues #2885, #2887, and #2890. The reversion removes the NZ format implementation from linear operations, test cases, and quantization configuration.

## Technical Significance
NZ format is Ascend's native compressed format that can improve memory bandwidth utilization, but the implementation in PR #2619 caused bugs in unquantized linear operations. This reversion indicates that the NZ format support for linear layers needs rework before it can be safely used in production. The issues suggest problems with format conversion or computation correctness.

## Related
- `technique-nz-format`, `kernel-linear-ascendc`, `technique-format-conversion`