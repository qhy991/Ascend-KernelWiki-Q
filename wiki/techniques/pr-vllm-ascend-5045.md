---
id: technique-pr-vllm-ascend-5045
title: "PR Insight: vllm-project/vllm-ascend #5045"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - speculative-decoding
  - suffix-decode
  - arctic-inference
  - dependencies
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5045"
---

# PR Insight: vllm-project/vllm-ascend #5045

**Title:** Add the requirement of arctic-inference which speculative decoding with suffix_decode

## Overview
This PR adds the arctic-inference library to requirements.txt and pyproject.toml, as the suffix spec decode method depends on it to work correctly.

## Technical Significance
Ensures the arctic-inference dependency is available by default for suffix-based speculative decoding functionality.

## Related
- `technique-speculative-decoding`
- `technique-suffix-decode`
- `kernel-arctic-inference`