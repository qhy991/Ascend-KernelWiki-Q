---
id: technique-pr-vllm-ascend-8372
title: "PR Insight: vllm-project/vllm-ascend #8372"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - quantization
  - w8a8
  - mxfp8
  - ascend950
  - moe
  - bugfix
  - dtype
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8372"
---

# PR Insight: vllm-project/vllm-ascend #8372

**Title:** [BugFix][Ascend950]  fix w8a8mxfp8 for moe

## Overview
This PR refactors the handling of quantization and scale data types by centralizing their definitions in mxfp_compat.py. It updates device_op.py to use these shared constants, ensuring consistent filtering for operators on Ascend950. The fix addresses MoE (Mixture of Experts) compatibility with W8A8 MXFP8 quantization on the latest Ascend hardware.

## Technical Significance
This refactoring improves code maintainability by centralizing dtype definitions and ensuring consistent operator filtering across Ascend950. The fix ensures proper MoE operation with advanced quantization schemes on new hardware. Centralizing dtype constants prevents inconsistencies and makes future hardware support easier to implement.

## Related
- `hw-ascend950`
- `technique-quantization`
- `technique-moe-optimization`