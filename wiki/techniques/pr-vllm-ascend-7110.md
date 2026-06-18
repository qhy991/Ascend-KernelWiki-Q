---
id: technique-pr-vllm-ascend-7110
title: "PR Insight: vllm-project/vllm-ascend #7110"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - model-runner-v2
  - graph-mode
  - refactoring
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7110"
---

# PR Insight: vllm-project/vllm-ascend #7110

**Title:** [Feature] support aclgraph for model runner v2

## Overview
Adds ACL graph mode support for model runner v2 as specified in RFC #5208. The implementation adapts to the newest vLLM main branch, supplies a unified interface of extra forward context for both model runner v1 and v2, and implements graph mode for the main model.

## Technical Significance
Extends ACL graph capabilities to model runner v2, enabling efficient graph-based inference with the new runner architecture. The unified forward context interface ensures compatibility across different runner versions while maintaining optimized performance.

## Related
- `technique-aclgraph`, `technique-model-runner-v2`, `technique-graph-mode`