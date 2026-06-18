---
id: technique-pr-vllm-ascend-6900
title: "PR Insight: vllm-project/vllm-ascend #6900"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - chunked-prefill
  - context-parallel
  - pcp
  - dcp
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6900"
---

# PR Insight: vllm-project/vllm-ascend #6900

**Title:** feat(attention_cp): support chunked prefill for Qwen3Next with PCP&DCP

## Overview
Adds chunked prefill support for Qwen3Next models using both Pipeline Context Parallel (PCP) and Data Context Parallel (DCP) strategies. The implementation enables efficient processing of long sequences by splitting prefill workloads across multiple devices.

## Technical Significance
Improves long sequence handling for Qwen3Next models by enabling distributed chunked prefill across multiple devices. This reduces memory pressure and improves throughput for large prompt scenarios while maintaining compatibility with both PCP and DCP parallelization strategies.

## Related
- `technique-chunked-prefill`, `technique-context-parallel`, `technique-pcp`, `technique-dcp`