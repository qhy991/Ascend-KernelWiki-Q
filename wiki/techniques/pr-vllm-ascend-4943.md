---
id: technique-pr-vllm-ascend-4943
title: "PR Insight: vllm-project/vllm-ascend #4943"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - nz-format
  - quantization
  - w4a8
  - w8a8
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4943"
---

# PR Insight: vllm-project/vllm-ascend #4943

**Title:** fix nz for quantization

## Overview
This PR fixes NZ format handling for quantization. Since quantization operations rely on NZ format by force, the PR removes NZ format checks that were blocking quantization operators.

## Technical Significance
Removes unnecessary NZ format validation that was preventing quantized operators from running. Ensures W4A8 and W8A8 quantization can proceed with NZ format requirements met automatically.

## Related
- `technique-nz-format`
- `technique-w4a8-quantization`
- `technique-w8a8-quantization`
- `kernel-w4a8-dynamic`
- `kernel-w8a8-dynamic`