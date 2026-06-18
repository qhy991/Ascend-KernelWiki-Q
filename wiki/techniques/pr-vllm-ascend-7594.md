---
id: technique-pr-vllm-ascend-7594
title: "PR Insight: vllm-project/vllm-ascend #7594"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - chunk-gated-delta-rule
  - qwen3.5
  - 310p-fallback
  - pytorch-implementation
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7594"
---

# PR Insight: vllm-project/vllm-ascend #7594

**Title:** [310P]: add torch chunk gated delta rule and 910b parity ut

## Overview
This PR adds a PyTorch implementation of the chunk gated delta rule operator for Ascend 310P. Since 310P cannot use the NPU-specific fused operator, this provides a PyTorch fallback. The implementation includes parity unit tests with 910B to ensure correctness.

## Technical Significance
This fallback matters for 310P Qwen3.5 support. Chunk gated delta rule is a key operation in Qwen3.5's attention mechanism. The PyTorch implementation enables 310P to run Qwen3.5 models, with parity tests ensuring output matches 910B results. While slower than NPU kernels, it ensures functional compatibility on edge hardware.

## Related
- pattern-310p-compatibility
- technique-gdn