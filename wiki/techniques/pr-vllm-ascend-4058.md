---
id: technique-pr-vllm-ascend-4058
title: "PR Insight: vllm-project/vllm-ascend #4058"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3-next
  - nz-format
  - bugfix
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4058"
---

# PR Insight: vllm-project/vllm-ascend #4058

**Title:** [BugFix] Fixes Qwen3-Next enable nz accuracy problem

## Overview
This PR fixes accuracy problems when enabling NZ format for Qwen3-Next models. Due to precision issues with NZ format, the use of NZ has been globally disabled for the qwen3-next model to ensure correct generation results. The fix modifies utility functions and worker logic to skip NZ conversion for Qwen3-Next.

## Technical Significance
NZ format optimization is disabled for correctness when it causes precision issues. This trade-off prioritizes accuracy over memory savings for Qwen3-Next. The fix ensures users get correct results even if it means losing the memory benefits of NZ format for this specific model.

## Related
- `technique-nz-format`, `pattern-accuracy-fix`, `technique-qwen3-next`, `technique-data-format`