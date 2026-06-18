---
id: technique-pr-vllm-ascend-874
title: "PR Insight: vllm-project/vllm-ascend #874"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decode
  - v1-engine
  - rejection-sampler
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/874"
---

# PR Insight: vllm-project/vllm-ascend #874

**Title:** Spec decode support for V1 Engine

## Overview
This PR enables speculative decoding support in the V1 engine by rewriting the triton-based rejection_sampler.py using PyTorch (since Ascend doesn't support triton kernels). Currently supports the ngram algorithm, with eagle algorithm planned for future adaptation.

## Technical Significance
Speculative decoding accelerates inference by using a draft model, providing significant throughput improvements. The PyTorch-based implementation enables this optimization on Ascend hardware, though future work will implement it in AscendC for better performance. This is a key feature for high-throughput inference workloads.

## Related
- `technique-spec-decode`
- `kernel-rejection-sampler`
- `kernel-inference`