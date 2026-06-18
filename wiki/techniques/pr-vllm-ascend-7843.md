---
id: technique-pr-vllm-ascend-7843
title: "PR Insight: vllm-project/vllm-ascend #7843"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - precision
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7843"
---

# PR Insight: vllm-project/vllm-ascend #7843

**Title:** [v0.18.0][BugFix] Fix bug of precision when DSA-CP is enabled on GLM5

## Overview
This PR fixes a precision bug that occurs with DSA-CP (Disaggregated Service Architecture - Context Parallelism) enabled on GLM5 models when using certain additional communication methods. The fix is specific to version 0.18.0 and addresses accuracy issues in multi-GPU communication scenarios.

## Technical Significance
Context parallelism is essential for serving very long context models. The precision bug in DSA-CP mode would cause incorrect outputs, particularly for GLM5 models. The fix ensures that tensor communication and reduction operations maintain numerical precision across context-parallel devices, which is critical for model correctness in distributed inference setups.

## Related
- `kernel-attention`
- `technique-hccl-optimization`
- `pattern-context-parallelism`