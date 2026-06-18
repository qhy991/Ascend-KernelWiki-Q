---
id: technique-pr-sgl-kernel-npu-29
title: "PR Insight: sgl-project/sgl-kernel-npu #29"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - assign-cache
  - cache-optimization
  - ascendc
  - operator-fusion
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/29"
---

# PR Insight: sgl-project/sgl-kernel-npu #29

**Title:** [feat] Add assign cache op

## Overview
This PR adds an assign cache operator that optimizes assign_req_to_token_pool function for SGLang MTP scenarios, reducing execution time from ~8ms (torch native) to ~0.4ms (AscendC implementation). The operator supports torch.int8/int16/int32/int64 types and requires torch.int64 for index inputs.

## Technical Significance
Achieves 20x performance improvement over PyTorch native implementation for cache assignment operations. The AscendC kernel implementation demonstrates significant optimization potential for token pool management in inference scenarios. The operator is critical for efficient KV cache management in transformer inference.

## Related
- technique-cache-optimization
- technique-operator-fusion
- technique-token-pool-management