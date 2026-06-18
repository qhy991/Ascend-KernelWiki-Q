---
id: technique-pr-vllm-ascend-1135
title: "PR Insight: vllm-project/vllm-ascend #1135"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mla
  - multistream
  - pipeline-scheduling
  - deepseek-v2
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1135"
---

# PR Insight: vllm-project/vllm-ascend #1135

**Title:** Support multistream of MLA vector operations

## Overview
This PR implements multi-stream execution for Multi-Head Latent Attention (MLA) vector operations to overlap computation and improve performance. The implementation moves vector operations like RMS normalization, RoPE, and matrix multiplications to a secondary stream, enabling better GPU utilization. The feature is controlled by `torchair_graph_config.enable_multistream_mla` configuration.

## Technical Significance
Multi-stream execution enables parallel execution of independent operations, reducing idle time on Ascend NPUs. By overlapping vector operations with matrix computations, this PR improves throughput for DeepSeek-V2 models. The implementation carefully handles dependency constraints, keeping IndexByTensor operators in the main stream due to graph fusion optimization limitations.

## Related
- `technique-mla`
- `technique-pipeline-scheduling`
- `technique-multistream`
- `technique-deepseek-v2`