---
id: technique-pr-sgl-kernel-npu-442
title: "PR Insight: sgl-project/sgl-kernel-npu #442"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - token-bitmask
  - speculative-decoding
  - json-schema
  - ascendc
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/442"
---

# PR Insight: sgl-project/sgl-kernel-npu #442

**Title:** feat: add apply_token_bitmask operator

## Overview
This PR implements an AscendC-based apply_token_bitmask operator for structured JSON output in speculative decoding, replacing a CPU fallback implementation. The operator achieves significant performance improvements, reducing average latency from 4.48ms to 0.171ms in single-concurrency and improving TTFT from 157.7ms to 107.5ms in 16-concurrency tests.

## Technical Significance
The NPU-based bitmask operator eliminates CPU fallback bottlenecks in structured generation scenarios, enabling efficient JSON schema validation during speculative decoding. The 26x latency improvement demonstrates the value of hardware-accelerated token masking for constrained text generation.

## Related
- `kernel-apply-token-bitmask`, `technique-speculative-decoding`, `technique-json-generation`