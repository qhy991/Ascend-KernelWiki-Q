---
id: technique-pr-vllm-ascend-923
title: "PR Insight: vllm-project/vllm-ascend #923"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-cache
  - v1-engine
  - revert
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/923"
---

# PR Insight: vllm-project/vllm-ascend #923

**Title:** [Bugfix][kvcache] revert multiple kv cache groups

## Overview
This PR reverts multiple KV cache groups related changes because the feature was reverted in the upstream vLLM project. The changes affected attention, MLA, and model runner V1 components.

## Technical Significance
Reverting features that were removed upstream ensures alignment with vLLM's direction and prevents maintaining unsupported functionality. This reflects the importance of tracking upstream changes and ensuring vllm-ascend stays compatible with vLLM's architectural decisions.

## Related
- `kv-cache`
- `kernel-attention`
- `kernel-mla`