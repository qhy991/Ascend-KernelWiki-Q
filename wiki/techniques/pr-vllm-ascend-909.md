---
id: technique-pr-vllm-ascend-909
title: "PR Insight: vllm-project/vllm-ascend #909"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - mla
  - nz-format
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/909"
---

# PR Insight: vllm-project/vllm-ascend #909

**Title:** update attention nz and mla nz(Improve TPOP 6ms performance)

## Overview
This PR improves TPOP performance by 6ms through NZ format optimizations. It converts W_UV and W_UK_T to NPU format in mla_v1.py and layer.weight to NPU format in w8a8.py, enabling better utilization of Ascend's NZ data layout.

## Technical Significance
NZ format is Ascend's optimized data layout that improves memory access patterns and compute efficiency. Converting attention and MLA weights to NZ format reduces memory bandwidth requirements and improves cache utilization, directly translating to better inference throughput (6ms TPOP improvement).

## Related
- `kernel-attention`
- `kernel-mla`
- `technique-nz-format`