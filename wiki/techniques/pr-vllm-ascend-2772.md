---
id: technique-pr-vllm-ascend-2772
title: "PR Insight: vllm-project/vllm-ascend #2772"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - layernorm
  - quantization
  - operator-fusion
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2772"
---

# PR Insight: vllm-project/vllm-ascend #2772

**Title:** [main] addrmsnorm + quant fusion optim in Dense Models

## Overview
This PR fuses the `addrmsnorm` operation with W8A8 quantization operators to improve performance in dense models. The fusion reduces kernel launch overhead and improves memory locality for better NPU utilization.

## Technical Significance
Operator fusion is a key optimization technique for reducing memory access and kernel launch overhead. Fusing layer normalization with quantization is particularly beneficial for dense models, improving throughput and reducing latency in quantized inference on Ascend NPU.

## Related
- `kernel-layernorm`
- `technique-operator-fusion`
- `kernel-quantization`
- `technique-fusion-optimization`