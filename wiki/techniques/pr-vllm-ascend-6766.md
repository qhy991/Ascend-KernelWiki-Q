---
id: technique-pr-vllm-ascend-6766
title: "PR Insight: vllm-project/vllm-ascend #6766"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - speculative-decoding
  - parallel-drafting
  - ascendc
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6766"
---

# PR Insight: vllm-project/vllm-ascend #6766

**Title:** [feat][spec decode]Unified draft parallel

## Overview
This PR implements unified parallelized speculative decoding for VLLM Ascend, supporting schemes like Pard and P-Eagle simultaneously. It adds an AscendC copy_and_expand_eagle_inputs operator that outperforms Triton with TTFT -20.4% and TPOT -9.24% improvements.

## Technical Significance
Significantly improves speculative decoding throughput by 98.58% (36.75 to 72.98 tok/s) through parallel draft execution. The AscendC implementation provides better hardware utilization compared to Triton, with consistent acceptance rates matching NVIDIA GPU performance.

## Related
- `technique-speculative-decoding`