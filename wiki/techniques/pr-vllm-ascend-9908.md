---
id: technique-pr-vllm-ascend-9908
title: "PR Insight: vllm-project/vllm-ascend #9908"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - quantization
  - tensor-parallel
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9908"
---

# PR Insight: vllm-project/vllm-ascend #9908

**Title:** [BugFix][Quantization]: NPU MoE quantization methods support TP only.

## Overview
This PR fixes NPU MoE quantization methods to support tensor parallelism (TP) only, addressing compatibility issues with MoE models under quantization when using tensor parallel distribution.

## Technical Significance
Resolves quantization compatibility for NPU MoE models by ensuring quantization methods work correctly with tensor parallelism. Fixes issues where MoE quantization failed or produced incorrect results when TP was enabled, improving support for quantized MoE inference.

## Related
- `technique-moe`, `technique-quantization`, `technique-tensor-parallel`, `kernel-matmul`