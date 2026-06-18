---
id: technique-pr-dsv4-dsa-cp
title: "PR Insight: DeepSeek-V4-Flash DSA-CP on A5"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek
  - sparse-attention
  - quantization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10026"
---

# PR Insight: DeepSeek-V4-Flash DSA-CP on A5

**Source:** [vLLM-Ascend PR #10026](https://github.com/vllm-project/vllm-ascend/pull/10026)

This PR introduces critical adaptations to support **DeepSeek-V4-Flash** running under Context Parallelism (DSA-CP) specifically targeted for newer Ascend architectures (A5 / 910C series).

## Core Technical Shifts

### 1. Dynamic MX (Micro-Scaling) Quantization
DeepSeek V4 utilizes advanced MX quantization formats to maintain extreme precision while dropping memory footprints. The PR adds an A5-specific output projection path utilizing **Dynamic MX Quantization** coupled with the `npu_transpose_quant_batchmatmul` operator.
- **Why it matters:** Instead of static scaling factors, dynamic MX calculates scaling metadata on-the-fly per block, which requires specialized AscendC matrix-multiplication kernels that natively understand the MX metadata headers alongside the weights.

### 2. DeviceOperator Routing
Because Ascend 910B and Ascend 5 have different hardware capabilities (e.g., native MX support on newer chips), the PR routes the Dynamic Sparse Attention (DSA) metadata through an abstract `DeviceOperator` layer.
- This allows the DSA-CP path to dynamically select A5-compatible argument formats for:
  - Sparse Attention Metadata
  - Slot Mapping
  - KV Scatter
  - Indexer Quantization

### 3. Compressed KV Handling
Handling DeepSeek's compressed KV cache (like MLA) in a distributed Ring Attention (CP) setup requires extreme precision to avoid synchronization bottlenecks. The PR fixes DSA-CP metadata propagation, ensuring that sparse indices align correctly across the NPU mesh when HCCS All-Gather events occur.
