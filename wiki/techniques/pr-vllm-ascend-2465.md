---
id: technique-pr-vllm-ascend-2465
title: "PR Insight: vllm-project/vllm-ascend #2465"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mla
  - refactor
  - preprocessing
  - attention
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2465"
---

# PR Insight: vllm-project/vllm-ascend #2465

**Title:** [Refactor][WIP] Refactor mla_v1 by moving all MLA preprocessing ops into mla_v1 attention impl

## Overview
This PR refactors MLA v1 by moving all MLA preprocessing operations into the mla_v1 attention implementation to better support fused kernels, multi-stream, and communication optimizations. The implementation adds 347 lines and removes 208 lines from `vllm_ascend/attention/mla_v1.py` and updates related files.

## Technical Significance
This refactoring aggregates all attention layer operations together, enabling better kernel fusion, multi-stream support, and communication optimizations. The new architecture doesn't consider torchair specifically, so it was merged after torchair-related MLA code was isolated. Performance benchmarks show maintained or improved performance after the refactor.

## Related
- `kernel-mla-v1`, `kernel-attention-v1`, `technique-operator-fusion`, `technique-multi-stream`