---
id: technique-pr-vllm-ascend-2888
title: "PR Insight: vllm-project/vllm-ascend #2888"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - weight-loading
  - hccl
  - netloader
  - p2p
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2888"
---

# PR Insight: vllm-project/vllm-ascend #2888

**Title:** [Misc] Add a model loader that utilizes HCCL for weight loading

## Overview
This PR introduces Netloader, a new model loading mechanism that leverages high-bandwidth P2P direct transfer between NPU cards using HCCL for faster weight loading. The implementation includes comprehensive documentation, timing diagrams, and test coverage.

## Technical Significance
Significant performance improvement for model loading by using HCCL P2P transfers instead of CPU-based loading. This reduces initialization time, especially for large models in multi-card scenarios. Netloader directly transfers weights between NPU cards using high-bandwidth interconnects, bypassing the CPU bottleneck and accelerating model startup.

## Related
- `technique-hccl-optimization`, `technique-weight-loading`, `hw-hccs`