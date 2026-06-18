---
id: technique-pr-catlass-239
title: "PR Insight: ascend/catlass #239"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - fp8
  - matmul
  - gemm
  - memory
  - performance
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/239"
---

# PR Insight: ascend/catlass #239 (add fp8 matmul)

## Overview
This PR introduces native Float8 (FP8) Matrix Multiplication (Matmul) support to the `ascend/catlass` library. CATLASS, as a CUTLASS-style C++ template library for Huawei Ascend NPUs, enables modular assembly of GEMM operations. With this update, it expands its `GemmType` template definitions to incorporate FP8 formats (such as E4M3/E5M2), tapping directly into the underlying hardware acceleration features of the Ascend 910B series.

## Technical Analysis

### FP8 Matrix Multiplication in CATLASS
By adding FP8 GEMM, this PR addresses a core requirement for high-efficiency Large Language Model (LLM) inference. Matrix multiplication templates in CATLASS (e.g., `Gemm::Block::BlockMmad`) now likely support an instantiation pathway where the layout mapping and cube unit tiling (L1 block tile and L0 MMA slice) accommodate FP8 elements. 

### Performance & Memory Implications
1. **Memory Bandwidth:** FP8 uses half the memory of FP16/BF16, heavily accelerating memory-bound layers and reducing L1/L0 caching pressure during the double-buffering (ping-pong) sequence.
2. **Compute Throughput:** Ascend's Cube unit provides enhanced throughput for FP8 MMA operations. Wrapping this in CATLASS allows upper-level operators to leverage optimal FRACTAL_NZ layout swizzling natively.

### Ecosystem Impact
This implementation is pivotal for subsequent integrations in down-stream repositories:
* **vLLM-Ascend & SGLang:** Allows native W8A8 (Weight-8 Activation-8) kernel compilation directly from CATLASS templates rather than requiring rigid, monolithic AscendC operators.
* **ModelLink & MindSpeed:** Accelerates the MoE and standard FFN linear layers when applying post-training quantization.

## Conclusion
Adding FP8 Matmul in CATLASS bridges a critical gap for Ascend optimization, supplying the necessary foundational C++ block templates for developers building low-latency, high-throughput quantized LLM serving pipelines.
