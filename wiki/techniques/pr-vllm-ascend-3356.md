---
id: technique-pr-vllm-ascend-3356
title: "PR Insight: vllm-project/vllm-ascend #3356"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - nz-format
  - quantization
  - moe
  - attention
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3356"
---

# PR Insight: vllm-project/vllm-ascend #3356

**Title:** [Feat]Unquantized Linear to nz and control all nz-cast

## Overview
Currently, when executing to the Linear layer of models in vLLM-Ascend, the weights format is ND in unquantized case and skipped ascend case.

## Technical Significance
Converts unquantized Linear layer weights to NZ format and controls all NZ cast operations for better Cube unit utilization.

## Related
- `hw-cube-unit`
- `technique-quantization`
- `technique-moe-routing`
