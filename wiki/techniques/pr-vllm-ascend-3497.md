---
id: technique-pr-vllm-ascend-3497
title: "PR Insight: vllm-project/vllm-ascend #3497"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - hccl-optimization
  - aclgraph
  - decode
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3497"
---

# PR Insight: vllm-project/vllm-ascend #3497

**Title:** [Fix] Refactor dummy attention metadata creation

## Overview
The `force_attention` parameter is designed for flash infer kernel warmup, we don't actually need it on Ascend device (at least for now).And it tends to make things more complicated. So we replace the `force_attention` parameter with `aclgraph_runtime_mode` in the attention metadata creation logic.

## Technical Significance
Refactors dummy attention metadata creation to improve code clarity and maintainability.

## Related
- `technique-aclgraph`
