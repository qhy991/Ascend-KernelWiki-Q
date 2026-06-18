---
id: technique-pr-vllm-ascend-1321
title: "PR Insight: vllm-project/vllm-ascend #1321"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - spec-decode
  - ci
  - testing
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1321"
---

# PR Insight: vllm-project/vllm-ascend #1321

**Title:** [CI/UT][bugfix] fix v0 spec decode

## Overview
This PR fixes bugs in V0 speculative decode implementation across multiple spec decode methods (EAGLE, Medusa, MLP, MTP, Ngram) and improves CI test stability.

## Technical Significance
Resolves correctness and stability issues in V0 spec decode by fixing worker implementation, multi-step worker logic, and test utilities. The comprehensive test coverage ensures that all spec decode variants work correctly on Ascend. This is critical for maintaining spec decode functionality in production inference.

## Related
- `technique-spec-decode`
- `technique-eagle`
- `technique-medusa`