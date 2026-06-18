---
id: technique-pr-vllm-ascend-773
title: "PR Insight: vllm-project/vllm-ascend #773"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - chunked-prefill
  - attention
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/773"
---

# PR Insight: vllm-project/vllm-ascend #773

**Title:** [Bugfix] Fix output tensor shape in vanilla_chunked_prefill and update import paths for model_loader

## Overview
This PR fixes output tensor shape issues in the `vanilla_chunked_prefill` function and updates import paths for model_loader. The changes ensure correct tensor dimensions during chunked prefill processing and maintain proper module imports.

## Technical Significance
Correct tensor shapes are critical for chunked prefill operations, which optimize long sequence processing. The fix prevents shape mismatch errors and ensures compatibility with updated vLLM codebase structure.

## Related
- `kernel-attention`
- `technique-chunked-prefill`