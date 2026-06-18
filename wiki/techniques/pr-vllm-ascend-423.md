---
id: technique-pr-vllm-ascend-423
title: "PR Insight: vllm-project/vllm-ascend #423"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - speculative-decoding
  - mla
  - worker
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/423"
---

# PR Insight: vllm-project/vllm-ascend #423

**Title:** [v0.7.3]spec decode MultiStepWorker support TP1DraftModelRunner fully

## Overview
This PR enables NPU multi-step prepare in MultiStepWorker for speculative decoding, adds MLA support to TP1DraftModelRunner, and fixes input_positions handling. The implementation removes is_cuda_like() checks and uses Ascend-specific draft model runner.

## Technical Significance
Enables proper NPU execution in speculative decoding instead of falling back to CPU prepare paths. MLA support allows speculative decoding with DeepSeek's compressed attention. The input_positions fix ensures compatibility with MLA attention backends.

## Related
- technique-speculative-decoding
- technique-mla