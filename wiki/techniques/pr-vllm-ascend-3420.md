---
id: technique-pr-vllm-ascend-3420
title: "PR Insight: vllm-project/vllm-ascend #3420"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - moe
  - hccl-optimization
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3420"
---

# PR Insight: vllm-project/vllm-ascend #3420

**Title:** [Perf] move quant before allgather in Allgather EP

## Overview
move quant before allgather in Allgather EP, rely on https://github.com/vllm-project/vllm-ascend/pull/3334

## Technical Significance
Optimizes Allgather Expert Parallel by moving quantization before allgather to reduce communication overhead.

## Related
- `technique-quantization`
- `technique-moe-routing`
