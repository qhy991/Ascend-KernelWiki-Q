---
id: technique-pr-vllm-ascend-7368
title: "PR Insight: vllm-project/vllm-ascend #7368"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3.5
  - split-qkv
  - rmsnorm
  - rope
  - operator-fusion
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7368"
---

# PR Insight: vllm-project/vllm-ascend #7368

**Title:** [features]support split qkv rmsnorm rmope for qwen3.5

## Overview
This PR enables the split_qkv_rmsnorm_mrope fusion operator for Qwen3.5 full attention. The fusion combines QKV projection splitting, RMSNorm, and multi-dimensional rotary embedding into a single operator, reducing memory transfers and improving performance.

## Technical Significance
This operator fusion matters for Qwen3.5 inference efficiency on Ascend. By combining three operations (split QKV, RMSNorm, MRoPE) into one kernel, it reduces HBM accesses and improves utilization. The fusion eliminates intermediate tensors and synchronization points, particularly beneficial for the multi-dimensional RoPE used in Qwen3.5's attention mechanism.

## Related
- technique-operator-fusion
- technique-split-qkv
- pattern-rmsnorm