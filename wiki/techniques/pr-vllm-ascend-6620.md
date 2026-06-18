---
id: technique-pr-vllm-ascend-6620
title: "PR Insight: vllm-project/vllm-ascend #6620"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - fusion
  - graph-mode
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6620"
---

# PR Insight: vllm-project/vllm-ascend #6620

**Title:** [BugFix] Fix AddRMSNormQuant not taking effect

## Overview
This PR fixes a bug where the fused AddRMSNormQuant operator does not take effect in graph mode when there is no bias. The fix ensures proper fusion and application of the operator across all graph configurations.

## Technical Significance
Fixes operator fusion logic that was preventing the AddRMSNormQuant fusion from being applied in certain graph mode configurations. This ensures consistent quantization fusion behavior regardless of bias presence, improving performance and maintaining correctness.

## Related
- `technique-operator-fusion`
- `technique-quantization`