---
id: technique-pr-vllm-ascend-474
title: "PR Insight: vllm-project/vllm-ascend #474"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - speculative-decoding
  - testing
  - e2e
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/474"
---

# PR Insight: vllm-project/vllm-ascend #474

**Title:** [2/N][CI/UT] enable spec_decode UT

## Overview
This PR adds end-to-end tests for speculative decoding, covering compatibility, integration (TP2, TP4), logprobs, MEDUSA, MLP speculators, and ngram correctness. The test suite includes 3000+ lines of test code and comprehensive utilities.

## Technical Significance
Robust e2e testing for all speculative decoding modes on Ascend. Tests cover distributed scenarios, various speculator types, and correctness validation. Future work will add graph mode, preemption, quantization, and MTP tests as features mature.

## Related
- technique-speculative-decoding
- technique-testing