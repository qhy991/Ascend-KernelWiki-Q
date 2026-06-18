---
id: technique-pr-vllm-ascend-6270
title: "PR Insight: vllm-project/vllm-ascend #6270"
type: wiki-technique
architectures:
  - ascend310p
  - ascend910
  - ascend910b
tags:
  - vllm
  - kv-cache
  - allocator
  - ascend310p
  - refactoring
  - code-alignment
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6270"
---

# PR Insight: vllm-project/vllm-ascend #6270

**Title:** [Refact.]: refactoring 310p-kv cache allocator, align with main branch

## Overview
This PR refactors the Ascend310p KV cache allocator to align with the main branch implementation. The changes update `model_runner_310p.py` to match the KV cache allocation logic used in the main branch, ensuring consistency across different Ascend hardware versions. The refactoring maintains the same functionality while improving code maintainability and reducing divergence between hardware-specific implementations.

## Technical Significance
This refactoring improves code maintainability by aligning the Ascend310p-specific KV cache allocator with the main branch implementation. Reducing divergence between hardware-specific paths makes the codebase easier to maintain and ensures that improvements and fixes in the main branch can more easily be applied to the 310p implementation. The E2E testing on Qwen2.5-7B confirmed that functionality is preserved during the refactoring, ensuring that the alignment doesn't introduce any regressions for Ascend310p users.

## Related
- `technique-kv-cache-paging`, `technique-memory-allocation`, `technique-ascend310p`, `technique-code-alignment`