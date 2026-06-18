---
id: technique-pr-vllm-ascend-7779
title: "PR Insight: vllm-project/vllm-ascend #7779"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - w4a8
  - operator-fusion
  - ascendc
  - dispatch-combine
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7779"
---

# PR Insight: vllm-project/vllm-ascend #7779

**Title:** [Feature][Kernel add] Fuse W4A8 dispatch + FFN + combine into a single fused kernel

## Overview
This PR adds a fused AscendC kernel that combines W4A8 dispatch, FFN computation, and combine operations into a single kernel. The implementation includes comprehensive AscendC kernel code for W4A8 quantized MoE operations with optimized tiling and memory management.

## Technical Significance
Significantly improves MoE inference performance by fusing dispatch, FFN, and combine operations into a single kernel, reducing memory transfers and kernel launch overhead. The W4A8 quantization further reduces memory footprint while maintaining accuracy.

## Related
- `kernel-moe`, `technique-operator-fusion`, `pattern-w4a8-quantization`, `pattern-ascendc-kernel`, `technique-moe-optimization`, `pattern-dispatch-combine-fusion`