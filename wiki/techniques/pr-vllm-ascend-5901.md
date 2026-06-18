---
id: technique-pr-vllm-ascend-5901
title: "PR Insight: vllm-project/vllm-ascend #5901"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - gpt-oss
  - sink
  - swa
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5901"
---

# PR Insight: vllm-project/vllm-ascend #5901

**Title:** [Attention] add gpt-oss support

## Overview
This PR adds support for GPT-OSS models, including Sliding Window Attention (SWA) and Sink attention features. The implementation updates the attention_v1 module and adapts the MoE section to support bias and swiglu_out activations for GPT-OSS.

## Technical Significance
GPT-OSS requires specialized attention mechanisms for efficient long-context modeling. SWA allows the model to attend to a fixed window of recent tokens, while Sink attention focuses on early tokens. The PR implements these features in attention_v1.py, rotary_embedding.py, and activation.py. It also updates the fused_moe module to handle GPT-OSS-specific activation patterns. Testing shows 100% accuracy on AIME2024 benchmarks with the changes.

## Related
- `technique-attention`, `technique-swa`, `technique-sink-attention`, `technique-moe`