---
id: technique-pr-vllm-ascend-7440
title: "PR Insight: vllm-project/vllm-ascend #7440"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - causal-conv1d
  - qwen3.5
  - 310p-fallback
  - pytorch-implementation
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7440"
---

# PR Insight: vllm-project/vllm-ascend #7440

**Title:** [310p][feat.] add ops causal-conv1d

## Overview
This PR adds PyTorch implementations of causal_conv1d_fn and causal_conv1d_update operators for Ascend 310P. These operators are needed to adapt Qwen3.5 models to the 310P hardware, which cannot use the NPU-specific fused operators.

## Technical Significance
This fallback matters for 310P Qwen3.5 support. Causal conv1d is a core operation in state-space models like Mamba, used in Qwen3.5's architecture. Without these PyTorch implementations, 310P couldn't run Qwen3.5 models. While less efficient than NPU kernels, they enable functional support on edge hardware.

## Related
- pattern-310p-compatibility
- technique-state-space-models