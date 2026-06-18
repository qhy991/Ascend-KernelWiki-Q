---
id: technique-pr-vllm-ascend-5602
title: "PR Insight: vllm-project/vllm-ascend #5602"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - fia
  - attention
  - bugfix
  - gemma3
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5602"
---

# PR Insight: vllm-project/vllm-ascend #5602

**Title:** [Bugfix] Remove swa parameter of fia

## Overview
This PR removes the `swa` parameter from the FIA (Flash Incremental Attention) operator due to compatibility issues with headDim=256. The parameter caused errors for models like Gemma3 that use larger head dimensions, and will be re-incorporated when CANN provides proper support.

## Technical Significance
The temporary removal of the swa parameter ensures compatibility with models that use larger head dimensions while maintaining correctness. This demonstrates the importance of gradual feature rollout and compatibility testing when integrating new attention optimization features across different model architectures.

## Related
- `kernel-attention` (FIA attention kernels)
- `technique-fia` (Flash Incremental Attention)
- `kernel-gemma3` (Gemma3 model support)