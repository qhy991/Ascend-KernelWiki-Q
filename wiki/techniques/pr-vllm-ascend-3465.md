---
id: technique-pr-vllm-ascend-3465
title: "PR Insight: vllm-project/vllm-ascend #3465"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - moe
  - attention
  - hccl-optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3465"
---

# PR Insight: vllm-project/vllm-ascend #3465

**Title:** [Feat]Qwen3 Moe supports npu_add_rms_norm_quant op by default, update op with bias, resolve conflict with weight prefetch

## Overview
1.qwen3 moe uses add_rms_norm_quant op instead of 'add_rms_norm op and quant op' during quantization scene.

## Technical Significance
Enables Qwen3 MoE models to use npu_add_rms_norm_quant operator by default with bias support and resolves conflicts with weight prefetching.

## Related
- `hw-cube-unit`
- `technique-quantization`
- `technique-moe-routing`
