---
id: technique-pr-vllm-ascend-8030
title: "PR Insight: vllm-project/vllm-ascend #8030"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - triton
  - elementwise
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8030"
---

# PR Insight: vllm-project/vllm-ascend #8030

**Title:** [Performance][model_runner_v2]Add bad-words-kernel triton kernel and optimize performance

## Overview
This PR adds a new Triton-based implementation of the bad-words filtering kernel for model_runner_v2 in `vllm_ascend/worker/v2/sample/bad_words.py`. The new implementation achieves significant performance improvements over the reference vLLM implementation, with particular efficiency gains for larger sequence batches. Benchmarks show 30-50% improvement for larger batches (256 sequences) and end-to-end accuracy verified against reference implementation.

## Technical Significance
The optimized bad-words kernel is crucial for production inference where content safety filtering is mandatory. The Triton implementation on Ascend NPUs demonstrates how custom kernels can outperform reference implementations, achieving better throughput while maintaining identical outputs. The performance gains are most significant at scale: for 2048 requests with max 256 sequences, the new implementation achieves ~14.8ms vs ~57.9ms (3.9x speedup). This directly impacts inference throughput for safety-gated deployments.

## Related
- `kernel-elementwise` (Bad words filtering)
- `technique-triton` (Triton kernel optimization)
- `pattern-performance-optimization` (Benchmark improvements)