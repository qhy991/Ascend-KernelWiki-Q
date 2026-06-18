---
id: technique-pr-vllm-ascend-9228
title: "PR Insight: vllm-project/vllm-ascend #9228"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - deepseek-v4
  - attention
  - moe
  - quantization
  - operator-fusion
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9228"
---

# PR Insight: vllm-project/vllm-ascend #9228

**Title:** [Ops][Feature] Add DeepSeek V4 custom operators

## Overview
This PR ports a comprehensive set of DeepSeek V4 custom operators from a development branch, adding attention operations (compressor, inplace partial rotary mul, quant lightning indexer, sparse attention), GMM operations (grouped matmul SwiGLU quantization), and MoE operations (hc_post, hc_pre, gating top-k hash, scatter updates). The implementation includes complete AscendC kernel code for multiple architectures, tiling strategies, and torch binding integration.

## Technical Significance
This is a major feature addition that enables efficient DeepSeek V4 inference on Ascend hardware. The operators are highly optimized with multi-architecture support (arch32/arch35), advanced techniques like compute-communication overlap, and specialized handling for quantized workloads. The comprehensive implementation includes host-side tiling, kernel-level optimizations, and integration with the vLLM runtime.

## Related
- `technique-operator-fusion`
- `technique-cube-vector-overlap`
- `technique-hccl-optimization`
- `kernel-attention`
- `kernel-moe`