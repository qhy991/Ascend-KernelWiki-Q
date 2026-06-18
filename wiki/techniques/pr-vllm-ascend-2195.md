---
id: technique-pr-vllm-ascend-2195
title: "PR Insight: vllm-project/vllm-ascend #2195"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - quantization
  - communication-optimization
  - all2all
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2195"
---

# PR Insight: vllm-project/vllm-ascend #2195

**Title:** [main][Prefill Perf] Optimize Quantized MoE Performance by Reducing All2All Communication

## Overview
This PR significantly optimizes quantized MoE performance by changing the order of quantization and communication operations. Instead of performing all2all on unquantized FP16/BF16 hidden states before quantization, it quantizes first on each EP rank and then sends the smaller quantized data, reducing communication volume by nearly 50%. Changes are in `vllm_ascend/quantization/w8a8_dynamic.py`.

## Technical Significance
This optimization dramatically reduces communication overhead in quantized MoE prefill by compressing data before transmission. The PR also includes a minor optimization to cast int inputs to float for argsort operations, forcing them to run on faster NPU cores instead of AICPU. The combined changes lead to significant performance gains in MoE quantization scenarios.

## Related
- `kernel-fused-moe-ascendc`, `technique-quantization-w8a8`, `technique-hccl-optimization`, `technique-communication-compression`