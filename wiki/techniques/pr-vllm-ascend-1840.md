---
id: technique-pr-vllm-ascend-1840
title: "PR Insight: vllm-project/vllm-ascend #1840"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - torchair
  - graph-mode
  - padding-strategy
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1840"
---

# PR Insight: vllm-project/vllm-ascend #1840

**Title:** [0.9.1][MTP V1]MTP model adapt torchair

## Overview
This PR adapts the MTP (Multi-Token Prediction) model to use torchair graph mode during the decode phase. The implementation uses a padding strategy where a fixed number of 1+MTP tokens are run per batch, and only the last index of accepted tokens is used for MTP hidden state generation.

## Technical Significance
Graph mode optimization for MTP models. The padding strategy enables efficient graph execution while handling the variable acceptance pattern of MTP tokens, reducing kernel launch overhead and improving decode throughput.

## Related
- `technique-mtp`
- `technique-torchair-graph`
- `technique-padding-strategy`