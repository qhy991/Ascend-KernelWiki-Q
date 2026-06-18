---
id: technique-pr-vllm-ascend-2474
title: "PR Insight: vllm-project/vllm-ascend #2474"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - gmm
  - nz-format
  - optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2474"
---

# PR Insight: vllm-project/vllm-ascend #2474

**Title:** [main] convert the format of gmm to nz

## Overview
This PR converts the GMM (grouped matrix multiplication) format to NZ format to improve performance. The implementation modifies `vllm_ascend/ops/fused_moe.py` to enable NZ format usage for GMM operations in MoE layers.

## Technical Significance
This optimization improves performance by leveraging the NZ format's better data locality and memory access patterns. Benchmark results on Qwen3 30B with 2k->20k context show token throughput improvement from 719.93 to 728.52 tok/s, demonstrating the benefits of NZ format for GMM operations.

## Related
- `kernel-fused-moe-ascendc`, `kernel-grouped-matmul-ascendc`, `technique-nz-format`, `technique-format-conversion`