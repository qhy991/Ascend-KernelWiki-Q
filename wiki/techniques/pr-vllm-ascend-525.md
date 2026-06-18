---
id: technique-pr-vllm-ascend-525
title: "PR Insight: vllm-project/vllm-ascend #525"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - sampling
  - topk
  - topp
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/525"
---

# PR Insight: vllm-project/vllm-ascend #525

**Title:** [0.7.3] Optimize apply_penalties & topKtopP for both V0/V1 Engine

## Overview
This PR optimizes sampling operations (apply_penalties and topK/topP) in both V0 and V1 engines by avoiding torch.scatter and matrix indexing operations. New ops files implement NPU-optimized sampling kernels.

## Technical Significance
Major performance improvement: decoding time reduced from 300ms to 50ms (6x speedup) for Qwen2.5-72B at concurrency 40. Custom NPU kernels avoid PyTorch's generic scatter/indexing overhead, critical for high-concurrency inference.

## Related
- technique-sampling
- technique-topk
- technique-topp