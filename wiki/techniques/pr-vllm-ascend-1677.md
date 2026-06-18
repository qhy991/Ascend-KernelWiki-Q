---
id: technique-pr-vllm-ascend-1677
title: "PR Insight: vllm-project/vllm-ascend #1677"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - paged-attention
  - graph-mode
  - aclgraph
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1677"
---

# PR Insight: vllm-project/vllm-ascend #1677

**Title:** [0.9.1][2/N][Feat] Restore paged attention kernel in Full Graph for performence

## Overview
This PR restores paged attention kernel in full graph mode (aclgraph) to improve performance.

## Technical Significance
Re-enables paged attention optimization within aclgraph's full graph compilation, improving memory efficiency and throughput for long-sequence inference. This restores performance parity between graph and eager modes for paged attention workloads.

## Related
- `kernel-attention`
- `technique-paged-attention`
- `technique-aclgraph`