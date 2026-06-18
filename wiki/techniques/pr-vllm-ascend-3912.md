---
id: technique-pr-vllm-ascend-3912
title: "PR Insight: vllm-project/vllm-ascend #3912"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - aclgraph
  - bugfix
  - spec-decoding
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3912"
---

# PR Insight: vllm-project/vllm-ascend #3912

**Title:** [0.11.0][MTP][Aclgraph] Fix the support aclgraph with MTP

## Overview
This PR fixes two breaks in ACLGraph support for MTP in v0.11.0: (1) DeepSeek MTP lacked the `support_torch_compile` decorator needed for ACLGraph, and (2) There was a device-to-host synchronization in the original MTP forward that prevented graph capture. The fix adds the missing decorator and removes the d2h sync, enabling MTP to run in ACLGraph mode.

## Technical Significance
Device-to-host synchronizations break graph capture by forcing CPU-GPU synchronization. The fix enables ACLGraph optimization for MTP in v0.11.0, which is critical for performance. Adding the `support_torch_compile` decorator allows the graph capture framework to properly handle MTP model components. This fix enables MTP to benefit from graph mode optimizations.

## Related
- `technique-mtp`, `technique-aclgraph`, `technique-graph-capture`, `technique-synchronization`