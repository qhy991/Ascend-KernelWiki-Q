---
id: technique-pr-vllm-ascend-1848
title: "PR Insight: vllm-project/vllm-ascend #1848"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - upstream-sync
  - ci-fix
  - refactoring
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1848"
---

# PR Insight: vllm-project/vllm-ascend #1848

**Title:** [Bugfix] Fix broken CI to follow pooler and attention refactor

## Overview
This PR fixes broken CI builds caused by upstream vLLM refactoring in pooler (#20927) and attention (#20466) modules. The fix adapts the Ascend-specific code to the new upstream structure while keeping CI functional.

## Technical Significance
Upstream synchronization maintenance. The vLLM upstream refactors affect the attention and pooler modules, requiring Ascend-specific adaptations to maintain compatibility and keep CI passing.

## Related
- `kernel-attention-ascendc`
- `technique-upstream-sync`
- `technique-ci-fix`