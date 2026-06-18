---
id: technique-pr-vllm-ascend-5854
title: "PR Insight: vllm-project/vllm-ascend #5854"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - triton
  - penalty
  - performance
  - multimodal
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5854"
---

# PR Insight: vllm-project/vllm-ascend #5854

**Title:** model runner v2 support triton of penalty

## Overview
This PR optimizes the penalty operator performance in the model runner v2 by implementing a Triton kernel. Testing on Qwen2.5-7B-VL shows the operator time is reduced by 90% compared to the previous implementation.

## Technical Significance
The penalty operator is critical for controlling token generation quality during inference. By implementing a Triton kernel, the PR achieves significant performance improvements while maintaining correctness. The optimization is particularly beneficial for multimodal vision-language models where penalty calculations add overhead to the generation pipeline. The fix adds a new Triton implementation in the penalties.py module and includes unit tests for validation.

## Related
- `technique-triton`, `technique-generation-optimization`