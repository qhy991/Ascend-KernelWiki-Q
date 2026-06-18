---
id: technique-pr-vllm-ascend-6715
title: "PR Insight: vllm-project/vllm-ascend #6715"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - data-parallel
  - xlite
  - qwen3-moe
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6715"
---

# PR Insight: vllm-project/vllm-ascend #6715

**Title:** [Feat]Xlite Qwen3 MoE Support Data Parallel

## Overview
This PR adds data parallel support for Qwen3-MoE models in Xlite environments. It enables combining expert parallelism with data parallelism, allowing for larger scale deployments across multiple devices.

## Technical Significance
Enables scalable Qwen3-MoE inference by supporting both expert parallelism and data parallelism simultaneously. This provides flexibility for large-scale deployments requiring distributed computation across multiple device groups.

## Related
- `kernel-moe`