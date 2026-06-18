---
id: technique-pr-vllm-ascend-9900
title: "PR Insight: vllm-ascend #9900"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - chunked prefill
  - scheduling
  - mtp
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9900"
---

# [Performance] Improve CPP performance on var-len seqence

## Overview
PR #9900 in the `vllm-project/vllm-ascend` repository improves the Chunked Prefill (CPP) performance specifically on variable-length sequences. It also addresses functional issues when combining CPP with Multi-Token Prediction (MTP).

## Architectural Explanations

### Chunked Prefill (CPP) on Variable-Length Sequences
Chunked Prefill (CPP) is a technique used to mitigate the latency constraints during prefilling for LLMs by breaking down large prefill sequences into smaller chunks. This allows the system to process both prefill and decode stages within the same execution cycle, leading to better resource utilization and throughput. 

In variable-length scenarios, naive scheduling can lead to performance degradation due to uneven workloads and suboptimal batching. This PR introduces a new **time budget-based scheduling strategy**, which dynamically allocates computational resources according to the actual workload constraints rather than fixed token quotas. This significantly enhances the handling of variable-length sequences.

### Multi-Token Prediction (MTP) Compatibility
Multi-Token Prediction (MTP) is a speculative decoding method that predicts multiple future tokens simultaneously to accelerate decoding. The PR addresses a functional issue where enabling both Chunked Prefill and MTP caused incorrect state management or validation errors in previous versions. By stabilizing the interaction between CPP and MTP, the system can benefit from both efficient prefill chunking and accelerated generation, maintaining seamless inference scaling.

## Impact
- **Performance**: Enhances system efficiency in var-len sequence contexts via refined time-budget scheduling for chunked prefill.
- **Bugfix**: Resolves functional conflicts between CPP and MTP, ensuring stability when both optimizations are enabled.
