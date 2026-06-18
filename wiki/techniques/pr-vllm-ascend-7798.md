---
id: technique-pr-vllm-ascend-7798
title: "PR Insight: vllm-project/vllm-ascend #7798"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - ascendc
  - causal-conv1d
  - custom-op
  - mamba
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7798"
---

# PR Insight: vllm-project/vllm-ascend #7798

**Title:** [Feature] [310p] Add npu_causal_conv1d_310 AscendC Custom Op

## Overview
This PR adds an AscendC custom operator for causal convolution 1D operations on Ascend 310P. The implementation includes comprehensive AscendC kernel code with optimized tiling and memory management for causal convolution workloads.

## Technical Significance
Enables efficient causal convolution 1D operations on Ascend 310P using optimized AscendC kernels, essential for Mamba and state-space model inference with proper hardware acceleration.

## Related
- `kernel-causal-conv1d`, `pattern-mamba-architecture`, `pattern-ascendc-kernel`, `technique-custom-operator`, `pattern-state-space-models`