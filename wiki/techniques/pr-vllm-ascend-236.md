---
id: technique-pr-vllm-ascend-236
title: "PR Insight: vllm-project/vllm-ascend #236"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - speculative-decoding
  - mtp
  - deepseek
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/236"
---

# PR Insight: vllm-project/vllm-ascend #236

**Title:** v0.7.3 Add MTP support for deepseek

## Overview
This PR adds Multi-Token Prediction (MTP) support for DeepSeek v3/r1 models, enabling speculation with num_speculative_tokens=1. Implementation includes patches for metrics and rejection sampling, plus attention and worker modifications.

## Technical Significance
MTP is DeepSeek's speculative decoding technique that predicts multiple tokens ahead. This PR implements the rejection sampling logic and metric tracking on Ascend, enabling faster inference by speculating and verifying multiple tokens.

## Related
- technique-speculative-decoding
- technique-mtp