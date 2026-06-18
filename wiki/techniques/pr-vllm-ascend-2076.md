---
id: technique-pr-vllm-ascend-2076
title: "PR Insight: vllm-project/vllm-ascend #2076"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mtp
  - torch
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2076"
---

# PR Insight: vllm-project/vllm-ascend #2076

**Title:** [BUGFIX][0.9.1] Fix MTP torch mode with DP problem

## Overview
This PR fixes a bug in the MTP (Multi-Token Prediction) torch mode when combined with data parallelism. The issue caused incorrect token proposal behavior in distributed inference scenarios, affecting model accuracy and generation quality.

## Technical Significance
MTP is a critical performance optimization for large language models. Ensuring correct behavior in DP scenarios is essential for production deployments that require both accuracy and throughput. This fix maintains the benefits of MTP while supporting distributed execution.

## Related
- `technique-mtp`
- `technique-distributed`
- `technique-speculative-decoding`
- `kernel-deepseek-mtp`