---
id: technique-pr-vllm-ascend-6151
title: "PR Insight: vllm-project/vllm-ascend #6151"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - structured-output
  - dependency
  - xgrammar
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6151"
---

# PR Insight: vllm-project/vllm-ascend #6151

**Title:** [Bugfix] Fix structured outputs errors: `TypeError: apply_token_bitmask_inplace_cpu()`

## Overview
This PR fixes structured output errors caused by incompatible function arguments to `apply_token_bitmask_inplace_cpu()` in the xgrammar library. The fix updates dependencies (pyproject.toml, requirements.txt) to use a compatible xgrammar version and adjusts E2E test workflows.

## Technical Significance
Structured outputs use grammar-constrained decoding via xgrammar's bitmask operations. The TypeError occurred when the CPU kernel received arguments in an incompatible format. This fix ensures version compatibility between vLLM's structured output implementation and xgrammar's CPU kernel interface, preventing runtime crashes during grammar-constrained generation.

## Related
- `technique-structured-output`, `technique-grammar-constrained-decoding`