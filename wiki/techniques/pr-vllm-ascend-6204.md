---
id: technique-pr-vllm-ascend-6204
title: "PR Insight: vllm-project/vllm-ascend #6204"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mm
  - attention
  - padding
  - parallelization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6204"
---

# PR Insight: vllm-project/vllm-ascend #6204

**Title:** [MM][Perf] Parallelize Q/K/V padding in AscendMMEncoderAttention for better performance

## Overview
This PR optimizes Q/K/V padding in `AscendMMEncoderAttention` by stacking QKV tensors first and padding them in a single kernel launch instead of three serial padding operations. The optimization reduces TTFT by 3.15% and increases peak throughput by 4.20%.

## Technical Significance
Vision-language models require QKV padding to 128 dimensions for optimal NPU performance. Previously, Q, K, and V were padded separately, requiring three `aclnnConstantPadNd` launches. By stacking first and padding together, kernel launch overhead is significantly reduced, demonstrating that operator fusion and batch reduction are critical for MM attention performance.

## Related
- `technique-mm-attention`, `technique-operator-fusion`, `technique-kernel-launch-optimization`