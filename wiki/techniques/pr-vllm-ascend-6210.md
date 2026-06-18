---
id: technique-pr-vllm-ascend-6210
title: "PR Insight: vllm-project/vllm-ascend #6210"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - inductor
  - quantization
  - rms-norm
  - operator-fusion
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6210"
---

# PR Insight: vllm-project/vllm-ascend #6210

**Title:** [Inductor][v0.13.0]Adapt AddRmsNormQuant pass to new addrmsnormBias operator

## Overview
This PR adapts the AddRmsNormQuant fusion pass to work with the new addrmsnormBias operator. PR #5790 changed the default operator to addrmsnormBias when custom ops are enabled, requiring this update to the Inductor compilation pass for v0.13.0.

## Technical Significance
The AddRmsNormQuant pass fuses RMS normalization with quantization for INT8 inference. With the new addrmsnormBias operator (from PR #6140), the fusion pattern matching needs to be updated to recognize the fused add+rmsnorm+bias operator. This ensures quantization fusion works correctly with the new operator, maintaining performance for quantized inference workloads.

## Related
- `technique-operator-fusion`, `technique-quantization`, `technique-inductor`, `technique-layernorm`