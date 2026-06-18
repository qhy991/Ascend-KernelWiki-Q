---
id: technique-pr-vllm-ascend-9271
title: "PR Insight: vllm-project/vllm-ascend #9271"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - a5
  - ascendc
  - attention
  - operator-fusion
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9271"
---

# PR Insight: vllm-project/vllm-ascend #9271

**Title:** [Feature][Ops] Add A5 custom operator build support

## Overview
This PR adds comprehensive build support for A5 custom operators, including indexer compression epilog, KV compression, quantized sparse attention with shared KV, and lightning indexer operations. The implementation includes complete CMake build configuration, AscendC kernel implementations for multiple architectures, and host-side tiling logic.

## Technical Significance
Adding A5 build support enables the deployment of highly optimized custom operators on A5 hardware, expanding the supported device ecosystem. The operators implement advanced features like MXFP8 support, sparse attention patterns, and efficient KV cache compression, which are critical for performance in modern LLM inference.

## Related
- `technique-operator-fusion`
- `hw-cube-unit`
- `hw-vector-unit`
- `kernel-attention`