---
id: technique-pr-vllm-ascend-9441
title: "PR Insight: vllm-project/vllm-ascend #9441"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek-v4
  - dsa
  - multistream
  - overlap
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9441"
---

# PR Insight: vllm-project/vllm-ascend #9441

**Title:** [Feature] DeepSeekV4 DSA indexer_select_qli cv multistream overlap

## Overview
This PR implements multistream compute vector overlap for the indexer_select_qli operation in DeepSeek V4 DSA (DeepSeek Sparse Attention). The changes affect DSA attention implementation and DSA operators to enable parallel execution across multiple streams.

## Technical Significance
Multistream overlap maximizes GPU utilization by allowing different operations to execute concurrently on different streams. This optimization is particularly impactful for indexer selection operations which can be overlapped with other computation, improving overall inference throughput.

## Related
- `kernel-attention`
- `technique-cube-vector-overlap`
- `technique-pipeline-scheduling`