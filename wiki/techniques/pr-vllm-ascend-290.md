---
id: technique-pr-vllm-ascend-290
title: "PR Insight: vllm-project/vllm-ascend #290"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - sdpa
  - encoder
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/290"
---

# PR Insight: vllm-project/vllm-ascend #290

**Title:** [Attn] Support encoder-only attention with torch sdpa

## Overview
This PR adds support for encoder-only attention using PyTorch's scaled dot-product attention (SDPA). The implementation adds 46 lines and removes 17 lines from attention.py, enabling models without decoder components.

## Technical Significance
Encoder-only models (like BERT) require different attention patterns than encoder-decoder models. This PR enables such models on Ascend by leveraging torch SDPA, expanding the range of supported architectures.

## Related
- kernel-attention