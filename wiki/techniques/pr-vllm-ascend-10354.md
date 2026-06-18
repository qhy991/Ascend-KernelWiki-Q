---
id: technique-pr-vllm-ascend-10354
title: "PR Insight: vllm-project/vllm-ascend #10354"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-cache
  - prefix-cache
  - deepseek
  - quantization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10354"
---

# PR Insight: vllm-project/vllm-ascend #10354

**Title:** [Feature][DSv4] Support compressor block size [32,64,128] to improve automatic prefix cache hit rate

## Overview
This PR makes the DeepSeek V4 compressor KV-cache block_size configurable (32/64/128) instead of being hard-coded to 128. The implementation uses a lookup table that scales the MLA/SWA/C4-state/C128-state block sizes and page-size padding together. A smaller block size reduces the alignment requirement of the compressed KV cache, allowing more prompt prefixes to hit the prefix cache and improving automatic prefix cache hit rates. Benchmarks show that block_size 32 achieves 87.49% HBM hit rate compared to 45.31% for block_size 128, with corresponding throughput improvements (8906 vs 6612 tok/s).

## Technical Significance
This feature significantly improves prefix cache effectiveness for DeepSeek V4 workloads. The configurable block size allows users to trade off between cache granularity and alignment overhead. Smaller block sizes provide finer cache-key granularity, leading to higher automatic prefix cache hit rates and better throughput for workloads with many shared prefixes. The lookup table approach ensures that all related KV cache structures (MLA, SWA, C4-state, C128-state) scale consistently with the selected block size.

## Related
- `technique-kv-cache-paging`
- `technique-prefix-cache`
- `technique-deepseek`
- `technique-quantization`