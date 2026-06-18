---
id: technique-pr-vllm-ascend-2062
title: "PR Insight: vllm-project/vllm-ascend #2062"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - distributed
  - torchair
  - optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2062"
---

# PR Insight: vllm-project/vllm-ascend #2062

**Title:** [main][refractor] Refractor forward metadata retrieval across DP nodes to reduce redundant padding.

## Overview
This PR refactors cross-DP (Data Parallel) decoding metadata aggregation to eliminate redundant token padding. The optimization conditionally applies padding only when in decode phase with TorchAir graph mode enabled, avoiding unnecessary padding operations in prefill phase or when graph mode is disabled.

## Technical Significance
Reducing redundant padding across DP nodes improves memory efficiency and computation overhead in distributed inference. The conditional padding strategy ensures optimal performance for both graph-based and eager execution modes, while maintaining correctness for prefill and decode phases.

## Related
- `technique-distributed`
- `technique-torchair`
- `technique-pipeline-scheduling`
- `technique-data-reuse`