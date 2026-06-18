---
id: technique-pr-vllm-ascend-2713
title: "PR Insight: vllm-project/vllm-ascend #2713"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mtp
  - memory
  - optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2713"
---

# PR Insight: vllm-project/vllm-ascend #2713

**Title:** perf : optimize memory for deepseek mtp

## Overview
This PR optimizes memory usage for DeepSeek MTP (Multi-Token Prediction) in TorchAir mode by removing temporary tensors. The reduction in memory footprint allows for larger batch sizes and more efficient utilization of NPU memory resources.

## Technical Significance
Memory optimization is critical for MTP workloads which require additional buffers for token proposal and verification. Reducing temporary tensor allocation improves cache efficiency and enables higher throughput in memory-constrained scenarios on Ascend NPU.

## Related
- `technique-mtp`
- `kernel-deepseek-mtp`
- `technique-memory-optimization`
- `technique-torchair`