---
id: technique-pr-vllm-ascend-425
title: "PR Insight: vllm-project/vllm-ascend #425"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - speculative-decoding
  - testing
  - ci
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/425"
---

# PR Insight: vllm-project/vllm-ascend #425

**Title:** [1/N][CI/UT] enable spec decode related UT

## Overview
This PR adds comprehensive unit tests for speculative decoding, including tests for batch expansion, dynamic spec decode, metrics, multi-step worker, ngram worker, spec decode worker, and utilities. The test suite includes over 2000 lines of test code.

## Technical Significance
Robust test coverage for speculative decoding features. The PR also updates CI to run vLLM from source and conditionally run spec decode tests only when related code changes, improving CI efficiency. Minor fixes to attention and platform modules.

## Related
- technique-speculative-decoding
- technique-testing