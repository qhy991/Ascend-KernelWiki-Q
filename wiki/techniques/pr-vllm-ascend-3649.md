---
id: technique-pr-vllm-ascend-3649
title: "PR Insight: vllm-project/vllm-ascend #3649"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - weight-prefetch
  - addrmsnormquant
  - layernorm
  - qkv-proj
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3649"
---

# PR Insight: vllm-project/vllm-ascend #3649

**Title:** [v0.11.0][Feat] Prefetching Attention QKV Linear Weight With `AddRmsNormQuant` Custom Op

## Overview
This PR implements `qkv_proj.weight` prefetching with the `AddRmsNormQuant` custom operator for the v0.11.0 branch. Previously, weight prefetching used the `Quant` op, but when `AddRmsNormQuant` was enabled (#3465), prefetching stopped working. This fix backports the main branch implementation (#3517) to v0.11.0, adding 22 lines to `vllm_ascend/ops/layernorm.py`.

## Technical Significance
Weight prefetching improves performance by overlapping data transfers with computation. When quantization operators are fused, the prefetching mechanism must adapt to use the fused operator. This fix ensures weight prefetching continues to work correctly when `AddRmsNormQuant` is enabled, maintaining performance benefits for quantized models like Qwen3-235B-A22B-W8A8.

## Related
- `technique-quantization`
- `technique-weight-prefetch`
- `technique-operator-fusion`