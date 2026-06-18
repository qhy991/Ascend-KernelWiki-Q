---
id: technique-pr-vllm-ascend-947
title: "PR Insight: vllm-project/vllm-ascend #947"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - multi-stream
  - deepseek
  - graph-mode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/947"
---

# PR Insight: vllm-project/vllm-ascend #947

**Title:** [perf]Support MOE Multi-stream in Deepseek

## Overview
This PR enables MOE multi-stream parallelism for DeepSeek models, which requires graph mode with mc2 enabled. Multi-stream allows overlapping computation and communication, improving MoE layer throughput.

## Technical Significance
Multi-stream parallelism improves MoE performance by overlapping expert computation with token dispatch/combine operations. This optimization is particularly effective for DeepSeek models and requires graph mode for proper scheduling, significantly improving inference throughput for MoE workloads.

## Related
- `kernel-moe`
- `technique-multi-stream`
- `technique-graph-mode`