---
id: technique-pr-vllm-ascend-2453
title: "PR Insight: vllm-project/vllm-ascend #2453"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - unit-tests
  - bugfix
  - correctness
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2453"
---

# PR Insight: vllm-project/vllm-ascend #2453

**Title:** feat: add mtp ut and fix some bugs

## Overview
This PR adds MTP mode unit tests and fixes several bugs discovered during testing. The implementation updates test files, mla attention, fused_moe, quantization config, torchair mla, and worker components to address various issues and improve test coverage.

## Technical Significance
The added unit tests improve confidence in MTP correctness and catch edge cases that were not previously tested. The bug fixes address various integration issues between MTP and other components (MLA, MoE, quantization, TorchAir), ensuring more reliable speculative decoding operation.

## Related
- `technique-speculative-decoding`, `kernel-mla-v1`, `kernel-fused-moe-ascendc`, `technique-unit-testing`