---
id: technique-pr-vllm-ascend-252
title: "PR Insight: vllm-project/vllm-ascend #252"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - speculative-decoding
  - eagle
  - ngram
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/252"
---

# PR Insight: vllm-project/vllm-ascend #252

**Title:** v0.7.3 support speculative decoding

## Overview
This PR adds comprehensive speculative decoding support on Ascend, including four modes: draft model speculation, n-gram matching from prompts, MLP speculators, and EAGLE-based draft models. Implementation includes worker patches and a 315-line draft model runner.

## Technical Significance
Speculative decoding can dramatically improve inference throughput by predicting multiple tokens in parallel and verifying them. This PR brings feature parity with GPU vLLM for all major speculation techniques on Ascend.

## Related
- technique-speculative-decoding
- technique-eagle