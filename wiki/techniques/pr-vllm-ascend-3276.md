---
id: technique-pr-vllm-ascend-3276
title: "PR Insight: vllm-project/vllm-ascend #3276"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - hccl-optimization
  - speculative-decoding
  - decode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3276"
---

# PR Insight: vllm-project/vllm-ascend #3276

**Title:** [Feat]Make full graph mode compalible with MTP

## Overview
Make the Full Graph mode can run with MTP.

## Technical Significance
Makes full graph mode compatible with MTP (Multi-Token Prediction) to enable graph-level optimizations for speculative decoding workloads.

## Related
- `hw-cube-unit`
- `technique-speculative-decoding`
