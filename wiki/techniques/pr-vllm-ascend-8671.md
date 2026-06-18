---
id: technique-pr-vllm-ascend-8671
title: "PR Insight: vllm-project/vllm-ascend #8671"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - attention
  - flash-attention
  - operator-fusion
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8671"
---

# PR Insight: vllm-project/vllm-ascend #8671

**Title:** [Performance] In scenarios A2 and A3, replace npu_fusion_attention with the _npu_flash_attention_unpad operator.

## Overview
This PR replaces the `npu_fusion_attention` operator with `_npu_flash_attention_unpad` in scenarios A2 and A3 (specific encoder attention scenarios). The change targets the `device_op.py` and `mm_encoder_attention.py` files to swap attention implementations for better performance. Testing on Qwen3.5 27B with GPQA shows maintained accuracy (85.35%) and improved throughput (290 to 300 tps at concurrency 22).

## Technical Significance
This performance optimization leverages the `_npu_flash_attention_unpad` operator, which is likely better optimized for the specific access patterns in encoder attention scenarios. The 3.4% throughput improvement while maintaining accuracy demonstrates the importance of selecting the right attention kernel for different use cases. The unpadded attention operator likely reduces memory overhead and improves cache utilization for encoder workloads.

## Related
- `kernel-attention-ascendc`
- `technique-operator-fusion`
- `hw-cube-unit`