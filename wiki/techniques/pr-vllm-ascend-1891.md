---
id: technique-pr-vllm-ascend-1891
title: "PR Insight: vllm-project/vllm-ascend #1891"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - multistream
  - w8a8
  - shared-experts
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1891"
---

# PR Insight: vllm-project/vllm-ascend #1891

**Title:** [Perf][MoE] Improve MoE multistream parallel performace.

## Overview
This PR redesigns shared expert multi-stream parallelism for w8a8-dynamic-quantized MoE to achieve better performance. The optimized shared expert multi-stream approach significantly improves throughput over the previous implementation.

## Technical Significance
Performance optimization for quantized MoE. Shared experts are common across all tokens, and optimized multistream parallelism for these experts is critical for overall MoE performance, especially in quantized scenarios.

## Related
- `technique-moe`
- `technique-multistream`
- `technique-w8a8-quantization`