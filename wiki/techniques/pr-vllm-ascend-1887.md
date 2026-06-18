---
id: technique-pr-vllm-ascend-1887
title: "PR Insight: vllm-project/vllm-ascend #1887"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - rope
  - deepseek
  - accuracy
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1887"
---

# PR Insight: vllm-project/vllm-ascend #1887

**Title:** [0.9.1][bugfix] V0.9.1 fix rope accruracy bug for deepseek model

## Overview
This PR fixes a RoPE accuracy problem in DeepSeek models with eager mode, which was introduced by interface changes in PR #1719. The fix restores correct RoPE computation for DeepSeek models.

## Technical Significance
Critical accuracy bugfix for DeepSeek models. RoPE is fundamental to transformer performance, and incorrect computation leads to degraded model quality. The fix addresses interface compatibility issues that broke RoPE.

## Related
- `kernel-rope-ascendc`
- `technique-deepseek`
- `technique-rope`