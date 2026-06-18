---
id: technique-pr-vllm-ascend-1721
title: "PR Insight: vllm-project/vllm-ascend #1721"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - layernorm
  - quantization
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1721"
---

# PR Insight: vllm-project/vllm-ascend #1721

**Title:** [0.9.1][BugFix] Fix the failure to recognize the actual type of quantization

## Overview
This PR fixes a bug in the layernorm operation where the system failed to correctly recognize the actual quantization type. The fix ensures the correct code branch is executed during quantized inference, specifically in the files `vllm_ascend/models/qwen3.py` and `vllm_ascend/ops/layernorm.py`.

## Technical Significance
Critical bugfix for quantization correctness. The quantization type detection failure could cause incorrect computation paths in layernorm operations, leading to potential accuracy issues in Qwen3 models. This fix ensures proper type inference and execution flow for quantized workloads.

## Related
- `kernel-layernorm-ascendc`
- `technique-quantization`