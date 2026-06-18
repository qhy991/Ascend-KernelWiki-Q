---
id: technique-pr-vllm-ascend-4168
title: "PR Insight: vllm-project/vllm-ascend #4168"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - torch-compile
  - inductor
  - operator-fusion
  - quantization
  - w8a8
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4168"
---

# PR Insight: vllm-project/vllm-ascend #4168

**Title:** [Fusion] Adopt inductor fusion and define quantization fusion pass

## Overview
This PR adopts torch.compile and inductor pattern matcher to automatically fuse optimization patterns, reducing maintenance burden from model duplication. The PR integrates `AddRMSNorm` and `Quant` operators, which improves inference speed for models using w8a8 quantization. Performance improvements are demonstrated for Qwen3-8B-W8A8 model.

## Technical Significance
Leveraging torch.compile and inductor pattern matching enables automatic fusion without manual model duplication. The AddRMSNorm+Quant fusion provides significant performance improvement for quantized models. This approach reduces long-term maintenance burden while providing hardware-specific optimizations for Ascend NPUs.

## Related
- `technique-operator-fusion`, `technique-torch-compile`, `technique-quantization`, `pattern-automatic-optimization`, `technique-w8a8`