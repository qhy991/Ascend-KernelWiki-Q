---
id: technique-pr-vllm-ascend-5491
title: "PR Insight: vllm-project/vllm-ascend #5491"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - operator-fusion
  - layernorm
  - quantization
  - npugraph
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5491"
---

# PR Insight: vllm-project/vllm-ascend #5491

**Title:** [Graph][Fusion] Add AddRMSNorm(with bias)

## Overview
This PR extends the npugraph_ex_passes module to support graph optimization for the add_rms_quant fused operator with bias terms. Building on prior work (PR #5011), it correctly registers and matches the fusion pattern into computation graphs, providing significant throughput improvements for W8A8 quantized models like Qwen3-235B-A22B-W8A8.

## Technical Significance
The AddRMSNorm fusion with bias support enables better operator fusion on Ascend NPU by combining addition, RMS normalization, and quantization operations into a single fused kernel. This reduces memory traffic and kernel launch overhead, improving inference throughput for quantized models while maintaining accuracy.

## Related
- `technique-operator-fusion` (AddRMSNorm fusion pattern)
- `kernel-layernorm` (RMS normalization)
- `kernel-quantization` (W8A8 quantization)
- `technique-npugraph` (NPU graph compilation)