---
id: technique-pr-vllm-ascend-3355
title: "PR Insight: vllm-project/vllm-ascend #3355"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - hccl-optimization
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3355"
---

# PR Insight: vllm-project/vllm-ascend #3355

**Title:** [Perf]Add YaRN custom op

## Overview
YaRN scaling is used to improve long seq accuracy for models like Qwen3. In vLLM, YaRN scaling refers to `YaRNScalingRotaryEmbedding` class which inherits from original `RotaryEmbedding`. Although `YaRNScalingRotaryEmbedding` does not rewrite the `forward` function of `RotaryEmbedding` , using YaRN on npu still run into the native implementation of foward in `RotaryEmbedding`, rather than forward_oot in vLLM-Ascend. Thus I register another custom op here to enable the oot implementation for YaRN in vLLM-Ascend, similar to #3151 .

## Technical Significance
Adds YaRN (Yet another RoPE extension) custom operator for supporting extended context windows in RoPE-based models.

## Related
- `hw-cube-unit`
