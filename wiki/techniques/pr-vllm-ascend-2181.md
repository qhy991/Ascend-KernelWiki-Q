---
id: technique-pr-vllm-ascend-2181
title: "PR Insight: vllm-project/vllm-ascend #2181"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen
  - vision-mlp
  - operator-fusion
  - vllm-upstream
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2181"
---

# PR Insight: vllm-project/vllm-ascend #2181

**Title:** [Bugfix] Follow vLLM Qwen-Moe/VL and KV Connector change to fix broken CI

## Overview
This PR fixes broken CI by adapting to upstream vLLM changes, including fusing gate and up projections in vision MLP (improving performance by reducing one matrix multiplication), updating ModelRunnerOutput parameters, and fixing Qwen MoE compatibility. Changes affect `vllm_ascend/models/qwen2_5_vl.py`, `vllm_ascend/models/qwen3_moe.py`, and worker files.

## Technical Significance
This maintenance PR ensures compatibility with upstream vLLM changes, particularly the vision MLP fusion that improves performance by eliminating a matrix multiplication operation. The fix maintains proper weight loading with `mlp.gate_up_proj` and uses `SiluAndMul` activation function, while also updating worker connector lifecycle tests.

## Related
- `kernel-matmul-ascendc`, `technique-operator-fusion`, `technique-vllm-upstream-sync`, `kernel-qwen-vision-mlp`