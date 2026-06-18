---
id: technique-pr-vllm-ascend-796
title: "PR Insight: vllm-project/vllm-ascend #796"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - embedding
  - vocab-parallel
  - custom-kernel
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/796"
---

# PR Insight: vllm-project/vllm-ascend #796

**Title:** add custom ascendc kernel vocabparallelembedding

## Overview
This PR adds a custom AscendC kernel implementation for vocab parallel embedding operations. It includes the kernel implementation in C++, CMakeLists build configuration, torch bindings, and comprehensive unit tests and benchmarks.

## Technical Significance
Custom AscendC kernels provide better performance than PyTorch operations by leveraging Ascend-specific hardware features. The vocab parallel embedding kernel is critical for distributed training and inference, enabling efficient embedding lookups across multiple devices.

## Related
- `kernel-embedding`
- `language-ascendc`
- `technique-vocab-parallel`