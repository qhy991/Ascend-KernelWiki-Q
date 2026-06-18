---
id: technique-pr-vllm-ascend-2403
title: "PR Insight: vllm-project/vllm-ascend #2403"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3-moe
  - qwen2.5
  - torchair
  - graph-mode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2403"
---

# PR Insight: vllm-project/vllm-ascend #2403

**Title:** qwen3_moe/qwen25 support torchair graph

## Overview
This PR adds TorchAir graph mode support for Qwen3-MoE and Qwen2.5 models. The implementation creates TorchAir-specific models in `vllm_ascend/torchair/models/qwen3_moe.py` (537 lines) and `qwen2.py` (364 lines), adds comprehensive tests, and updates attention and rotary embedding for TorchAir compatibility.

## Technical Significance
This integration enables Qwen3-MoE and Qwen2.5 models to benefit from TorchAir's graph compilation and execution, reducing host overhead and improving inference performance. The implementation includes proper configuration support for graph batch sizes, chunked prefill, and caching, making it production-ready for TorchAir deployments.

## Related
- `kernel-fused-moe-ascendc`, `kernel-qwen3-moe`, `kernel-qwen2.5`, `technique-torchair-integration`