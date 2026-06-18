---
id: technique-pr-vllm-ascend-9218
title: "PR Insight: vllm-project/vllm-ascend #9218"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - testing
  - gqa
  - precision-validation
  - mtp
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9218"
---

# PR Insight: vllm-project/vllm-ascend #9218

**Title:** [Test] add attention ut for attention_v1

## Overview
This PR introduces comprehensive unit tests for the attention_v1 GQA (Grouped Query Attention) implementation on Ascend NPUs. The test suite in `tests/ut/attention/test_attention_v1_precision.py` validates numerical correctness by comparing NPU output against PyTorch's scaled_dot_product_attention (SDPA) as a golden baseline across 16 batch specifications.

## Technical Significance
The test suite covers standard attention scenarios (decode-only, prefill-only, mixed), encoder-only scenarios, and MTP (Multi-Token Prediction) scenarios with various sequence lengths (32-4096 tokens), batch sizes (1-32), and tensor parallel sizes (1, 2, 4). This comprehensive validation ensures numerical correctness of attention implementations across different execution patterns and provides regression testing for future changes to the GQA backend.

## Related
- `kernel-attention-ascendc`, `technique-flash-attention`, `technique-speculative-decoding`