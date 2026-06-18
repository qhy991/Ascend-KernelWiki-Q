---
id: technique-pr-vllm-ascend-9363
title: "PR Insight: vllm-project/vllm-ascend #9363"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mixed-precision
  - rotary-embedding
  - bugfix
  - ascendc
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9363"
---

# PR Insight: vllm-project/vllm-ascend #9363

**Title:** [BugFix][Ops] Support mixed precision rotary mul

## Overview
This PR adds support for mixed-precision rotary position embedding multiplication in the inplace_partial_rotary_mul operator. The changes include updates to the operator definition, protocol implementations, tiling strategies, and kernel-level handling for different rotary embedding register patterns.

## Technical Significance
Mixed-precision rotary embedding allows for more flexible and potentially more efficient attention implementations by supporting different precision combinations for position embeddings. This fix enables correct behavior when using mixed-precision configurations, improving the robustness of attention implementations.

## Related
- `kernel-attention`
- `technique-format-conversion`