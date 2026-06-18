---
id: technique-pr-sgl-kernel-npu-177
title: "PR Insight: sgl-project/sgl-kernel-npu #177"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - dispatch
  - npu-computation
  - optimization
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/177"
---

# PR Insight: sgl-project/sgl-kernel-npu #177

**Title:** calculate dispatch normal input parameters using npu instead of cpu

## Overview
Optimizes dispatch normal input parameter calculation by moving computations from CPU to NPU. The changes include calculating send_token_idx in layout kernel, recv_count and recv_offset in notify dispatch kernel, and changing num_recv_tokens_per_expert_list from List to tensor.

## Technical Significance
This optimization significantly improves dispatch performance by reducing CPU-NPU data transfer and computation overhead. Benchmarks show improved bandwidth from 115.81 GB/s to 133.23 GB/s for dispatch and 98.46 GB/s to 101.20 GB/s for combine, with corresponding latency reductions. The NPU-side computation eliminates expensive CPU operations and data marshaling.

## Related
- `wiki-kernel-moe`
- `wiki-technique-npu-computation`
- `wiki-technique-data-transfer`
- `wiki-technique-optimization`