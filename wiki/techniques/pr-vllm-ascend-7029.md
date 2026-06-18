---
id: technique-pr-vllm-ascend-7029
title: "PR Insight: vllm-project/vllm-ascend #7029"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - w8a8c8
  - deepseek
  - glm5
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7029"
---

# PR Insight: vllm-project/vllm-ascend #7029

**Title:** [Perf][1/N] w8a8c8 support in dsv3.2/glm5

## Overview
Adds W8A8C8 quantization support for DeepSeek V3.2 and GLM5 models in pd-mix stage using lightning_indexer_quant operators. The implementation includes new quantization operators and configuration switches, with plans for future optimization using improved scatter operators and comprehensive PD-disaggregated scenario validation.

## Technical Significance
Introduces C8 (channel-wise) quantization for improved compression and performance on specific models. The phased approach prioritizes functionality with current operators while planning performance optimizations and broader scenario support as the infrastructure matures.

## Related
- `technique-quantization-w8a8`, `technique-c8-quantization`, `technique-deepseek`, `technique-glm5`