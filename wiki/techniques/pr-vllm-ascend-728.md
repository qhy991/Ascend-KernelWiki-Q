---
id: technique-pr-vllm-ascend-728
title: "PR Insight: vllm-project/vllm-ascend #728"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - w8a8
  - deepseek
  - memory
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/728"
---

# PR Insight: vllm-project/vllm-ascend #728

**Title:** support 32K model len on deepseek r1 W8A8

## Overview
This PR optimizes NPU memory usage for DeepSeek R1 W8A8 quantized models, enabling 32K context length support (previously limited to 16K due to OOM). Changes affect w8a8_dynamic.py.

## Technical Significance
Memory optimization is critical for long-context inference. The fix enables DeepSeek R1's full context window on Ascend by reducing peak memory usage in the dynamic W8A8 quantization path.

## Related
- technique-quantization
- technique-w8a8
- technique-deepseek