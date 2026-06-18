---
id: technique-pr-vllm-ascend-1328
title: "PR Insight: vllm-project/vllm-ascend #1328"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - deepseek-dbo
  - accuracy
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1328"
---

# PR Insight: vllm-project/vllm-ascend #1328

**Title:** [0.9.1][BugFix]fix accuracy in dbo after refactor MOE

## Overview
This PR fixes accuracy regression in DeepSeek-DBO models that occurred after the MoE refactoring in #1264.

## Technical Significance
Corrects numerical precision issues introduced during MoE code consolidation. The fix ensures that DeepSeek-DBO models maintain accuracy parity with the pre-refactor implementation, which is critical for production deployments requiring exact numerical consistency.

## Related
- `kernel-moe`
- `kernel-deepseek`