---
id: technique-pr-vllm-ascend-966
title: "PR Insight: vllm-project/vllm-ascend #966"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - memory-optimization
  - tensor-disposal
  - quantization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/966"
---

# PR Insight: vllm-project/vllm-ascend #966

**Title:** [Perf] Refactor tensor disposal logic to reduce memory usage

## Overview
This PR refactors tensor disposal logic using the `dispose_tensor` function from sglang, disposing of `hidden_states` and `residual` tensors once they're no longer used. It also avoids generating `self.inputs_embeds` in non-multimodal scenarios.

## Technical Significance
Memory optimization is critical for large model inference. This approach saves 1.3GB of NPU memory for DeepSeek-R1-W8A8 models under TP=16 and max-model-len=32768, significantly improving memory efficiency and enabling larger batch sizes or longer sequences.

## Related
- `technique-memory-optimization`
- `kernel-deepseek`
- `technique-quantization`