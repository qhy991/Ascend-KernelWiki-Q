---
id: technique-pr-vllm-ascend-2680
title: "PR Insight: vllm-project/vllm-ascend #2680"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - refactor
  - code-cleanup
  - quantizer
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2680"
---

# PR Insight: vllm-project/vllm-ascend #2680

**Title:** [1/N][Refactor][Quantization] remove redundant quantizer class

## Overview
This PR removes redundant quantizer classes (AscendQuantizer/LLMQuantizer) and replaces them with simpler map-based quantization method selection. The refactoring simplifies the codebase by removing 311 lines from quantizer.py and adding 222 lines to utils.py.

## Technical Significance
The refactoring improves code simplicity and maintainability by replacing class-based quantization method selection with map-based selection. This eliminates the need for AscendQuantizer and LLMQuantizer classes, making the code cleaner and easier to understand. The change is part 1 of an N-part quantization refactoring series.

## Related
- `technique-quantization`
- `technique-refactor`
- `technique-code-cleanup`