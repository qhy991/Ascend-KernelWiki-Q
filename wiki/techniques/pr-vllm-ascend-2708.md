---
id: technique-pr-vllm-ascend-2708
title: "PR Insight: vllm-project/vllm-ascend #2708"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mtp
  - deepseek
  - distributed
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2708"
---

# PR Insight: vllm-project/vllm-ascend #2708

**Title:** [FEATURE][MTP] Support MTP > 1

## Overview
This PR enables MTP (Multi-Token Prediction) with `num_speculative_tokens > 1` for DeepSeek models. The implementation supports various distributed configurations (DP1TP16, DP4TP4, DP2TP8) and includes TorchAir graph mode compatibility for improved performance.

## Technical Significance
Supporting MTP > 1 significantly improves inference throughput by proposing multiple tokens per step. This is particularly valuable for large-scale DeepSeek deployments where throughput is critical. The distributed support ensures scalability across multiple NPU devices.

## Related
- `technique-mtp`
- `kernel-deepseek-mtp`
- `technique-speculative-decoding`
- `technique-distributed`