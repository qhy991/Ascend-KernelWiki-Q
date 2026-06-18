---
id: technique-pr-vllm-ascend-3354
title: "PR Insight: vllm-project/vllm-ascend #3354"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - moe
  - hccl-optimization
  - speculative-decoding
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3354"
---

# PR Insight: vllm-project/vllm-ascend #3354

**Title:** bugfix for mtp when running torchair in a2

## Overview
when ops  torchair_fused_experts_with_mc2 is called, we need pass a tp group, but now it only pass when quantized scenario, we need also pass it when unquantized.

## Technical Significance
Fixes MTP compatibility issues when running in TorchAir environment on Ascend A2 devices.

## Related
- `technique-quantization`
- `technique-moe-routing`
- `technique-speculative-decoding`
