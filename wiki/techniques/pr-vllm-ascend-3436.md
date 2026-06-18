---
id: technique-pr-vllm-ascend-3436
title: "PR Insight: vllm-project/vllm-ascend #3436"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - hccl-optimization
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3436"
---

# PR Insight: vllm-project/vllm-ascend #3436

**Title:** fix pagedattention to support fullgraph.

## Overview
Calculate in advance the workspace memory size needed for the PagedAttention operator to avoid deadlocks during resource cleanup. This PR requires torch_npu version 0920 or newer.

## Technical Significance
Fixes PagedAttention implementation to support full graph mode for ACLGraph compilation compatibility.

## Related
- `hw-cube-unit`
