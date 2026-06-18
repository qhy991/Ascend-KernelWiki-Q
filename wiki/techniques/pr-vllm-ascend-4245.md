---
id: technique-pr-vllm-ascend-4245
title: "PR Insight: vllm-project/vllm-ascend #4245"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3-next
  - quantization
  - nz-format
  - triton
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4245"
---

# PR Insight: vllm-project/vllm-ascend #4245

**Title:** [Feat][BugFix]Support the Qwen3-Next-80B-A3B-Instruct quantization model&Fix the NZ issue

## Overview
This PR adds support for Qwen3-Next-80B-A3B-Instruct quantization models and fixes NZ format issues. Triton kernels don't support NZ data format, so weight conversion to NZ is skipped on the conv1d layer. The changes enable running quantized Qwen3-Next models generated with Modelslim.

## Technical Significance
Support for quantized Qwen3-Next models enables memory-efficient inference for large models. The NZ format fix prevents precision issues when using Triton kernels that don't support the format. Skipping NZ conversion on incompatible layers ensures correctness while maintaining performance benefits where NZ can be used.

## Related
- `technique-quantization`, `technique-qwen3-next`, `technique-nz-format`, `pattern-format-compatibility`, `technique-triton`