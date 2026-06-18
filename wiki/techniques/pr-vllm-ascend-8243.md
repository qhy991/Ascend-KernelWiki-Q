---
id: technique-pr-vllm-ascend-8243
title: "PR Insight: vllm-project/vllm-ascend #8243"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - sampling
  - min-p
  - triton
  - performance
  - partitioning
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8243"
---

# PR Insight: vllm-project/vllm-ascend #8243

**Title:** [Performance][model_runner_v2]:optimize the performance of the _min_p_kernel

## Overview
This PR optimizes the _min_p_kernel Triton operator used in sampling by adding an expanded_idx_mapping parameter and improving the core partitioning performance. The optimization focuses on the min-p sampling algorithm implementation, which is used to filter tokens based on minimum probability thresholds. The changes are applied to the kernel implementation and updated in the model runner patch.

## Technical Significance
Min-p sampling is an important sampling strategy that balances exploration and exploitation. Optimizing the partitioning performance improves overall sampling efficiency, which is critical for inference throughput. The PR demonstrates systematic Triton kernel optimization for sampling operations, adding configuration parameters to enable more efficient token filtering and candidate selection.

## Related
- `technique-sampling-optimization`
- `technique-triton-optimization`
- `technique-min-p-sampling`