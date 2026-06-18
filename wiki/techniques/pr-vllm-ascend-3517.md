---
id: technique-pr-vllm-ascend-3517
title: "PR Insight: vllm-project/vllm-ascend #3517"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - hccl-optimization
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3517"
---

# PR Insight: vllm-project/vllm-ascend #3517

**Title:** [Feat] Prefetching Attention QKV Linear Weight With `AddRmsNormQuant` Custom Op

## Overview
This PR [feat] prefetching attention qkv linear weight with `addrmsnormquant` custom op. It modifies core implementation files including vllm_ascend/ops/layernorm.py.

## Technical Significance
Implements attention QKV linear weight prefetching with AddRmsNormQuant custom operator for improved performance.

## Related
- `technique-quantization`
- `technique-kv-cache-paging`
