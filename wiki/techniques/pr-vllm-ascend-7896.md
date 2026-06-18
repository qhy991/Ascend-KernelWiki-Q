---
id: technique-pr-vllm-ascend-7896
title: "PR Insight: vllm-project/vllm-ascend #7896"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pipeline-parallelism
  - dynamic-chunking
  - long-context
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7896"
---

# PR Insight: vllm-project/vllm-ascend #7896

**Title:** [Feature][PP] Support Dynamic Chunk for Chunked Pipeline Parallelism

## Overview
This PR implements dynamic chunking for Chunked Pipeline Parallelism (CPP) to address computational efficiency issues when KV cache grows with long sequences. The feature profiles requests of different lengths, fits a functional relationship between sequence length and execution time, and calculates appropriate chunk sizes during scheduling to equalize batch execution time.

## Technical Significance
CPP is valuable for ultra-long context scenarios but suffers from empty slots as KV cache grows. Dynamic chunking optimizes this by adjusting chunk sizes based on execution time profiling. Performance results show 15% TTFT improvement for 256k sequences and better throughput for variable-length scenarios. This enables efficient serving of very long context models on Ascend NPUs.

## Related
- `pattern-pipeline-parallelism`
- `technique-profiling-optimization`
- `pattern-long-context-inference`