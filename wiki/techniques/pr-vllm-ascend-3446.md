---
id: technique-pr-vllm-ascend-3446
title: "PR Insight: vllm-project/vllm-ascend #3446"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - nz-format
  - quantization
  - moe
  - hccl-optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3446"
---

# PR Insight: vllm-project/vllm-ascend #3446

**Title:** [bugfix][torchair] fix missing weight nz cast for w13_weight in torchair_w8a8_dynamic.py

## Overview
Fix the issue of missing NZ conversion for quantized weights in GMM after moe_dispatch operator in torchair scenario, which does not involve aclgraph & single scenarios.

## Technical Significance
Fixes missing weight NZ cast for w13_weight in TorchAir W8A8 dynamic quantization to prevent accuracy errors.

## Related
- `technique-quantization`
- `technique-moe-routing`
- `technique-nz-tiling`
