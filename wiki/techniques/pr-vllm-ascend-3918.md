---
id: technique-pr-vllm-ascend-3918
title: "PR Insight: vllm-project/vllm-ascend #3918"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - qwen3-next
  - spec-decoding
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3918"
---

# PR Insight: vllm-project/vllm-ascend #3918

**Title:** [Feat] Adapted mtp function to Qwen3-next

## Overview
This PR adapts MTP (Multi-Token Proposal) functionality to Qwen3-Next model. The changes include updating attention logic, adding Qwen3-Next MTP model implementation, modifying causal_conv1d operations, and updating MTP proposer to work with Qwen3-Next architecture. The validation confirms that Qwen3-next and Qwen3-next-mtp produce identical generation results.

## Technical Significance
Adapting MTP to new model architectures requires understanding the model's attention mechanisms and causal convolution operations. Qwen3-Next has specific architectural patterns that require MTP integration to ensure correct speculative decoding. This enables performance improvements for Qwen3-Next models through speculative decoding while maintaining correctness.

## Related
- `technique-mtp`, `technique-spec-decoding`, `pattern-model-adaptation`, `technique-attention`