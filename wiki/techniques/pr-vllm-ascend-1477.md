---
id: technique-pr-vllm-ascend-1477
title: "PR Insight: vllm-project/vllm-ascend #1477"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - pangu-moe
  - w8a8c8
  - quantization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1477"
---

# PR Insight: vllm-project/vllm-ascend #1477

**Title:** support pangumoe w8a8c8 and docs

## Overview
This PR adds W8A8C8 (8-bit weight, 8-bit activation, 8-bit cache) quantization support for PanguMoE models and includes documentation updates.

## Technical Significance
Enables memory-efficient inference of PanguMoE models through comprehensive 8-bit quantization across weights, activations, and cache. The implementation updates attention, model, quantization configuration, and provides deployment documentation. This is critical for deploying large PanguMoE models on memory-constrained Ascend NPUs.

## Related
- `technique-w8a8-quantization`
- `kernel-moe`
- `kernel-pangu`