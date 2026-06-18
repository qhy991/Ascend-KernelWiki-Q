---
id: technique-pr-vllm-ascend-9728
title: "PR Insight: vllm-project/vllm-ascend #9728"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - communication
  - all2all
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9728"
---

# PR Insight: vllm-project/vllm-ascend #9728

**Title:** [BugFix] Optimize router experts in eager mode and fix communication handling

## Overview
This PR optimizes router experts in eager mode for MoE models (DeepSeek, Qwen MoE) by fixing implementation discrepancies of mc2 and all2all primitives. It resolves import errors, tensor split size mismatch exceptions, and adds comprehensive Unit Tests and End-to-End tests.

## Technical Significance
Improves hardware utilization on Ascend NPU for MoE models by ensuring proper communication handling (mc2/all2all/tensor splitting) in eager mode. Fixes bugs related to shared_experts and router_experts communication primitives, adding robust test coverage to prevent regressions.

## Related
- `technique-moe`, `technique-hccl-optimization`, `kernel-matmul`