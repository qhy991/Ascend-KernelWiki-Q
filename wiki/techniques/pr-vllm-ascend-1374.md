---
id: technique-pr-vllm-ascend-1374
title: "PR Insight: vllm-project/vllm-ascend #1374"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - documentation
  - qwen3
  - aclgraph
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1374"
---

# PR Insight: vllm-project/vllm-ascend #1374

**Title:** Doc Enhancement: Single NPU(Qwen3-8B) aclgraph mode + eager mode

## Overview
This PR enhances documentation for running Qwen3-8B on single NPU with both aclgraph and eager execution modes.

## Technical Significance
Improves user onboarding by providing clear deployment guidance for Qwen3-8B inference on single Ascend NPU. The documentation covers both aclgraph (graph-optimized) and eager modes, helping users choose the appropriate execution strategy based on their latency and flexibility requirements.

## Related
- `technique-aclgraph`
- `kernel-qwen3`