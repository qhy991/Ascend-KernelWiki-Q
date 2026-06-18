---
id: technique-pr-vllm-ascend-849
title: "PR Insight: vllm-project/vllm-ascend #849"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - chunked-prefill
  - mla
  - bugfix
  - deepseek
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/849"
---

# PR Insight: vllm-project/vllm-ascend #849

**Title:** [BugFix][0.7.3] Fix chunked prefill bugs in engine v1

## Overview
This PR fixes chunked prefill bugs when running DeepSeek models in the V1 engine and enables MLA (Multi-head Latent Attention) to use chunked prefill features. The changes are specifically for the v0.7.3 version.

## Technical Significance
Enabling chunked prefill for MLA allows DeepSeek models to process long sequences more efficiently by breaking them into chunks. This optimization reduces memory pressure and improves throughput for long-context workloads while maintaining compatibility with the v0.7.3 version.

## Related
- `technique-chunked-prefill`
- `kernel-mla`
- `kernel-deepseek`