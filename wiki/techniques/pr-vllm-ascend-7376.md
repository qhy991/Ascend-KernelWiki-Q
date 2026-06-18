---
id: technique-pr-vllm-ascend-7376
title: "PR Insight: vllm-project/vllm-ascend #7376"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - split-qkv
  - rmsnorm
  - rope
  - triton
  - operator-fusion
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7376"
---

# PR Insight: vllm-project/vllm-ascend #7376

**Title:** [OPS]add split_qkv_tp_rmsnorm_rope ops

## Overview
This PR introduces a fused Triton kernel split_qkv_tp_rmsnorm_rope for Minimax-m2.5. The implementation includes two kernels: _split_qkv_and_compute_local_qk_var_kernel for splitting QKV and computing local RMSNorm variance, and _apply_global_rmsnorm_kernel for applying global RMSNorm with TP all-reduce and Neox-style RoPE.

## Technical Significance
This operator fusion matters for Minimax-m2.5 inference efficiency on Ascend. The fusion combines QKV splitting, tensor-parallel RMSNorm (requiring TP all-reduce for variance), and rotary embedding into optimized Triton kernels. Benchmarks show ~23% TTFT improvement and ~38% throughput improvement at BS4, demonstrating significant gains from reducing memory transfers and synchronization.

## Related
- technique-operator-fusion
- technique-tensor-parallelism
- technique-triton
- pattern-rmsnorm