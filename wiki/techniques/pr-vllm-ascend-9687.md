---
id: technique-pr-vllm-ascend-9687
title: "PR Insight: vllm-project/vllm-ascend #9687"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - mla
  - quantization
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9687"
---

# PR Insight: vllm-project/vllm-ascend #9687

**Title:** [BugFix][MLA][Ascend950] Zero-init o_proj_input padding to prevent NaN propagation in quantization

## Overview
This PR fixes NaN propagation in MLA quantization by zero-initializing the `o_proj_input` padding segment. Previously, the buffer was allocated with graph-mode padded shape but only partially written, leaving uninitialized memory in padding that could contain NaN values propagating through downstream quantization (e.g., w8a8_mxfp8).

## Technical Significance
Prevents spurious token generation in Kimi models by making padding slots inert for quantization. Switching from uninitialized memory to `torch.zeros` ensures that padding values don't interfere with per-block quantization operations, eliminating precision degradation from garbage data in padded regions.

## Related
- `kernel-mla`, `technique-quantization`, `technique-mxfp8`