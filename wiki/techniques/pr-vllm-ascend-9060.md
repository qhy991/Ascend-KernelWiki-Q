---
id: technique-pr-vllm-ascend-9060
title: "PR Insight: vllm-project/vllm-ascend #9060"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - flash-attention
  - attention
  - inference
  - training
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9060"
---

# PR Insight: vllm-project/vllm-ascend #9060

**Title:** [Feature] support Flash Attention 3 (FA3) for training-inference consistency.

## Overview
This PR introduces Flash Attention 3 (FA3) support on Ascend NPUs, providing a new attention backend that ensures training-inference consistency. The implementation includes the FA3 backend (`vllm_ascend/attention/fa3_v1.py`), integration into the platform's attention selector (`vllm_ascend/platform.py`), and comprehensive test suites for both end-to-end correctness and unit testing of custom FA3 operations.

## Technical Significance
FA3 represents a significant advancement in attention computation efficiency and numerical consistency between training and inference workloads on Ascend NPUs. The integration enables users to leverage FA3 by setting `attention_backend="FLASH_ATTN"` and enabling `VLLM_BATCH_INVARIANT=1`. The implementation includes rigorous validation through end-to-end tests comparing FA3 output against Fused Infer Attention (FIA) across various prompt lengths and batch sizes.

## Related
- `kernel-attention-ascendc`, `technique-flash-attention`, `technique-operator-fusion`