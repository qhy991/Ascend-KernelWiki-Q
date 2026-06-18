---
id: technique-pr-vllm-ascend-5482
title: "PR Insight: vllm-project/vllm-ascend #5482"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - shared-expert
  - resource-management
  - quantization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5482"
---

# PR Insight: vllm-project/vllm-ascend #5482

**Title:** [Feature] Support fine-grained shared expert overlap

## Overview
This PR introduces fine-grained control over shared expert overlap in MoE (Mixture of Experts) models to prevent resource contention. The implementation modifies the Fused MoE module, communication methods, token dispatcher, and quantization configurations to support more efficient shared expert utilization on Ascend NPU.

## Technical Significance
Fine-grained shared expert overlap optimization improves MoE performance by better managing resource allocation between shared and routed experts, preventing bottlenecks and improving NPU utilization. This is particularly important for large-scale MoE models where shared expert routing can become a performance bottleneck.

## Related
- `pattern-moe` (MoE patterns and operations)
- `technique-fused-moe` (Fused MoE implementation)
- `kernel-moe` (MoE kernel operations)
- `kernel-quantization` (MoE quantization integration)