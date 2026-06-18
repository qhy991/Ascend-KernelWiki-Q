---
id: technique-pr-vllm-ascend-1204
title: "PR Insight: vllm-project/vllm-ascend #1204"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - pangu
  - inference
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1204"
---

# PR Insight: vllm-project/vllm-ascend #1204

**Title:** Support Pangu Pro MoE model

## Overview
This PR adds support for the Pangu Pro MoE model (arXiv:2505.21411) in vLLM-Ascend. The implementation includes a new model file `vllm_ascend/models/pangu_moe.py` with 639 lines of code, along with integration into the model registry and MoE operator infrastructure.

## Technical Significance
Support for Pangu Pro MoE expands vLLM-Ascend's model compatibility to include Huawei's Pangu series, which is important for Chinese NLP applications. The implementation demonstrates proper integration of new MoE architectures into the Ascend inference stack, enabling efficient inference on Huawei's NPUs.

## Related
- `technique-moe`
- `technique-pangu`
- `technique-fused-moe`