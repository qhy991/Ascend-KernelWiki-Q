---
id: technique-pr-sgl-kernel-npu-420
title: "PR Insight: sgl-project/sgl-kernel-npu #420"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - causal-conv1d
  - prefill
  - mamba
  - qwen3-next
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/420"
---

# PR Insight: sgl-project/sgl-kernel-npu #420

**Title:** add Conv1d prefill ops

## Overview
This PR adds AscendC implementations of causal_conv1d operators for prefill operations in linear attention models like Qwen3-Next and Qwen3.5. The comprehensive implementation includes host-side inference, tiling, kernel code, and stub files for both half and bfloat16 dtypes, with extensive test coverage for validation.

## Technical Significance
Providing optimized prefill conv1d operations is critical for efficient processing of long sequences in Mamba-style attention models. The AscendC implementation leverages hardware-specific optimizations for both major data types, supporting the diverse precision requirements of modern transformer architectures.

## Related
- `kernel-causal-conv1d`, `kernel-mamba`, `kernel-prefill`, `technique-ascendc-implementation`