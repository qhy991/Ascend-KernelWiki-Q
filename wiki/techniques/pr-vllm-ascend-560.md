---
id: technique-pr-vllm-ascend-560
title: "PR Insight: vllm-project/vllm-ascend #560"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - speculative-decoding
  - testing
  - chunk-prefill
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/560"
---

# PR Insight: vllm-project/vllm-ascend #560

**Title:** [0.7.3][5/N][CI/UT]add spec decode e2e UT && [BUGFIX]fix chunk prefill bug

## Overview
This PR adds multistep correctness tests (801 lines) and enables EAGLE test cases with modelscope weights. It also fixes a chunked prefill bug where attention masks with single elements weren't supported.

## Technical Significance
Expands speculative decoding test coverage to multistep scenarios. The chunk prefill fix ensures correctness when processing single-token attention masks, important for edge cases in chunked prefill.

## Related
- technique-speculative-decoding
- technique-chunk-prefill