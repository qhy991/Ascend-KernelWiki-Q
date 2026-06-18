---
id: technique-pr-vllm-ascend-3068
title: "PR Insight: vllm-project/vllm-ascend #3068"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - deepseek
  - mtp
  - memory-allocation
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3068"
---

# PR Insight: vllm-project/vllm-ascend #3068

**Title:** [bugfix][torchair] fix wasted NPU memory buffer allocation for quantized deepseek with unquantized MTP layer

## Overview
This PR fixes abnormal NPU memory consumption when running quantized DeepSeek models with unquantized MTP layers. The issue was caused by calling dist.all_to_all_single without correct device process group arguments, wasting 2*HCCL_BUFFSIZE bytes of VRAM per call.

## Technical Significance
Correct process group specification is essential for collective communication operations. The memory waste could accumulate and cause OOM errors in production deployments. The fix ensures efficient memory usage when mixing quantized and unquantized layers, which is common in models like DeepSeek with specialized MTP layers.

## Related
- `kernel-deepseek-ascendc`, `kernel-quantization-ascendc`, `technique-hccl-optimization`