---
id: technique-pr-vllm-ascend-5324
title: "PR Insight: vllm-project/vllm-ascend #5324"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - triton
  - rejection-sampling
  - refactoring
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5324"
---

# PR Insight: vllm-project/vllm-ascend #5324

**Title:** [Refactor][Triton] Move reject sample triton kernels into ops/triton

## Overview
This PR refactors the codebase by moving reject sampling related Triton kernels from the sample module into the ops/triton directory. This reorganization improves code structure and aligns kernel implementations with other operators.

## Technical Significance
Consistent code organization improves maintainability and discoverability of kernel implementations. Moving rejection sampling kernels to ops/triton follows the established pattern for custom operators, making it easier to develop and optimize sampling kernels for Ascend NPUs.

## Related
- technique-triton-optimization
- technique-rejection-sampling
- technique-code-organization