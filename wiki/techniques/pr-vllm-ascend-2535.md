---
id: technique-pr-vllm-ascend-2535
title: "PR Insight: vllm-project/vllm-ascend #2535"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - torchair
  - refactor
  - separation
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2535"
---

# PR Insight: vllm-project/vllm-ascend #2535

**Title:** [4/N][refactor]delete torchair from quantization

## Overview
This PR completes the torchair quantization refactoring by removing torchair-related code from the general quantization files, after moving it to the dedicated torchair/quantization directory in PR #2504. The implementation removes 12 lines from `vllm_ascend/quantization/w4a8_dynamic.py` and 24 lines from `w8a8_dynamic.py`.

## Technical Significance
This refactoring completes the separation of torchair and non-torchair quantization code paths, significantly improving code organization. The cleaner separation makes it easier to maintain and evolve each quantization backend independently and reduces the risk of unintended interactions.

## Related
- `technique-quantization-w4a8`, `technique-quantization-w8a8`, `technique-torchair-integration`, `technique-backend-separation`