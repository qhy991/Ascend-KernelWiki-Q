---
id: technique-pr-vllm-ascend-2790
title: "PR Insight: vllm-project/vllm-ascend #2790"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decode
  - mtp
  - memory-optimization
  - deepseek
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2790"
---

# PR Insight: vllm-project/vllm-ascend #2790

**Title:** Deepseek Mtp model uses the lm_head and embedding from the main model

## Overview
This PR optimizes memory usage in the Deepseek MTP (Multi-Token Proposer) model by sharing the lm_head and embedding layers with the main model instead of loading duplicate copies. For Deepseek-R1 model with fp16 weights (129280×7168), this saves 3.45GB of GPU memory in pure data parallel scenarios.

## Technical Significance
Significant memory optimization for spec-decode workloads by reusing weight matrices between main model and MTP layer. The implementation uses torch.equal to identify identical matrices, then reuses them instead of creating temporary copies. This is particularly important for large language models like Deepseek-R1 where embedding and lm_head layers consume substantial memory.

## Related
- `technique-spec-decode`, `technique-memory-optimization`, `technique-weight-sharing`