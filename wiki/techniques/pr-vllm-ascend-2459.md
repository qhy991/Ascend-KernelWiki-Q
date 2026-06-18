---
id: technique-pr-vllm-ascend-2459
title: "PR Insight: vllm-project/vllm-ascend #2459"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mla
  - torchair
  - refactor
  - deepseek
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2459"
---

# PR Insight: vllm-project/vllm-ascend #2459

**Title:** [2/N][refactor] torchair deepseek mla backend refactor

## Overview
This PR moves the unified MLA backend implementation to the torchair folder and removes torchair-related code from `attention/mla_v1.py`, reducing it from 1.3k to 0.9k lines. The implementation creates `vllm_ascend/torchair/torchair_mla.py` (1319 lines) with comprehensive tests.

## Technical Significance
This refactoring isolates TorchAir-specific MLA implementation into a dedicated module, significantly reducing the size and complexity of the general MLA implementation. This improves code maintainability and makes it easier to evolve TorchAir and non-TorchAir MLA backends independently.

## Related
- `kernel-mla-v1`, `technique-torchair-integration`, `technique-code-refactor`, `kernel-deepseek-mla`