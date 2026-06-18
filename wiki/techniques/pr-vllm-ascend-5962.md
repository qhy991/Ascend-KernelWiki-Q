---
id: technique-pr-vllm-ascend-5962
title: "PR Insight: vllm-project/vllm-ascend #5962"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - shared-expert
  - overlap
  - feature
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5962"
---

# PR Insight: vllm-project/vllm-ascend #5962

**Title:** [0.13.0][Feature] Support fine-grained shared expert overlap

## Overview
This PR adds support for fine-grained shared expert overlap in MoE models. It's a cherry-pick of PR #5482 to the v0.13.0 release branch, enabling optimization where shared expert computations can overlap with routed expert computations.

## Technical Significance
Shared expert overlap allows MoE models to compute shared expert outputs in parallel with routed experts, reducing latency and improving throughput. Fine-grained control provides better resource utilization by enabling more granular scheduling of expert computations. This optimization is particularly beneficial for models with both shared and routed experts, improving overall inference performance.

## Related
- `technique-moe`, `technique-shared-expert`, `technique-overlap-optimization`