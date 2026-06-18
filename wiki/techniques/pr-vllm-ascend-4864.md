---
id: technique-pr-vllm-ascend-4864
title: "PR Insight: vllm-project/vllm-ascend #4864"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - custom-ops
  - compilation
  - env-var
  - cleanup
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4864"
---

# PR Insight: vllm-project/vllm-ascend #4864

**Title:** Remove COMPILE_CUSTOM_KERNELS env

## Overview
This PR removes the COMPILE_CUSTOM_KERNELS environment variable and enables csrc compilation by default. With more custom operators merged, the ability to disable custom kernel compilation is no longer needed.

## Technical Significance
Simplifies the build process by always compiling custom kernels. Users no longer need to explicitly enable custom operators through an environment variable, reducing configuration complexity and ensuring optimized operators are always available.

## Related
- `technique-custom-op`
- `technique-kernel-compilation`