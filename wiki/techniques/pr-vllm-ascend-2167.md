---
id: technique-pr-vllm-ascend-2167
title: "PR Insight: vllm-project/vllm-ascend #2167"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - tensor-parallelism
  - oproj
  - memory-optimization
  - graph-mode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2167"
---

# PR Insight: vllm-project/vllm-ascend #2167

**Title:** [feat]: oproj tensor parallelism in  pure DP and graph-mode scenarios.

## Overview
This PR introduces OProj matrix tensor parallelism to reduce memory consumption, only supporting graph mode in pure DP scenarios. The implementation adds 247 lines to `vllm_ascend/ops/linear.py`, modifies parallel state handling, and includes comprehensive test updates. Benchmark results show 5.8 GB NPU memory savings per rank with `oproj_tensor_parallel_size = 8` and 1 ms TPOT increase, with best performance at size 4.

## Technical Significance
This optimization enables splitting the o_proj matrix along the row dimension (head_num * head_dim) into multiple tensor parallel shards, reducing per-rank memory footprint significantly. The feature adds a new configuration option `oproj_tensor_parallel_size` and requires the head dimension to be divisible by this value. This is particularly valuable for large models where memory is a bottleneck.

## Related
- `kernel-matmul-ascendc`, `technique-tensor-parallelism`, `technique-memory-optimization`, `technique-graph-mode`