---
id: technique-pr-vllm-ascend-7398
title: "PR Insight: vllm-project/vllm-ascend #7398"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - gated-delta-rule
  - recurrent
  - 310p-fallback
  - pytorch-implementation
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7398"
---

# PR Insight: vllm-project/vllm-ascend #7398

**Title:** [310P]fused recurrent gated delta rule pytorch core and ut

## Overview
This PR adds a PyTorch implementation of the fused recurrent gated delta rule operator for Ascend 310P. Since 310P cannot use the NPU-specific fused operator, this provides a PyTorch fallback implementation to support models using gated delta rule mechanisms.

## Technical Significance
This fallback matters for 310P model coverage. The gated delta rule is used in state-space models like Mamba. Without this PyTorch implementation, 310P couldn't run these models. While slower than NPU kernels, it enables functional support on the edge-oriented 310P hardware for recurrent architectures.

## Related
- pattern-310p-compatibility
- technique-state-space-models