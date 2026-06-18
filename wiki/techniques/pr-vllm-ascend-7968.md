---
id: technique-pr-vllm-ascend-7968
title: "PR Insight: vllm-project/vllm-ascend #7968"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ci
  - quantization
  - w8a8
  - mtp
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7968"
---

# PR Insight: vllm-project/vllm-ascend #7968

**Title:** 【CI】add nightly cases: MiniMax-M2.5-W8A8 Qwen3.5-27B-w8a8 Qwen3.5-397B-A1…

## Overview
This PR adds nightly CI test cases for three quantized models on A3 hardware: Qwen3.5-27B W8A8, MiniMax-M2.5 W8A8, and Qwen3.5-397B W8A8 MTP. The additions include model configuration files and updates to the nightly test workflow to validate these models daily.

## Technical Significance
Regular CI testing of quantized models ensures that W8A8 (8-bit weight and activation) quantization paths continue to work correctly across codebase changes. The inclusion of both standard and MTP variants covers important execution paths. Daily testing provides early detection of regressions in quantization support for large-scale models like Qwen3.5-397B.

## Related
- `technique-quantization`
- `quantization-w8a8`
- `pattern-mtp`