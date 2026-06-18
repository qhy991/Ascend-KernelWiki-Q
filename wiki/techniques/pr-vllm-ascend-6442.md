---
id: technique-pr-vllm-ascend-6442
title: "PR Insight: vllm-project/vllm-ascend #6442"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - weight-prefetch
  - moe
  - mlp
  - inference
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6442"
---

# PR Insight: vllm-project/vllm-ascend #6442

**Title:** [Refactor] MLP weight prefetch to consistency with MoE Model's prefetching

## Overview
This PR refactors the MLP weight prefetch mechanism to be consistent with MoE model prefetching in both code structure and usage. It removes environment variables VLLM_ASCEND_ENABLE_PREFETCH_MLP, VLLM_ASCEND_MLP_DOWN_PREFETCH_SIZE, and VLLM_ASCEND_MLP_GATE_UP_PREFETCH_SIZE in favor of a unified configuration format using --additional-config with weight_prefetch_config parameters.

## Technical Significance
Standardizes the weight prefetch configuration interface across different model types (Dense MLP vs MoE), simplifying user configuration and maintenance. The refactoring unifies prefetch ratio settings (gate_up and down) into a single configuration structure, making the prefetch mechanism more maintainable and consistent.

## Related
- `technique-data-reuse`