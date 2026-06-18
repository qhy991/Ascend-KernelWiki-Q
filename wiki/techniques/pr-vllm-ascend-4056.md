---
id: technique-pr-vllm-ascend-4056
title: "PR Insight: vllm-project/vllm-ascend #4056"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3-next
  - nz-format
  - bugfix
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4056"
---

# PR Insight: vllm-project/vllm-ascend #4056

**Title:** [0.11.0] [Cherry-pick #4058] Fixes Qwen3-Next enable nz accuracy problem

## Overview
This PR is a cherry-pick to v0.11.0 of PR #4058, fixing Qwen3-Next accuracy problems when NZ format is enabled. The fix addresses precision issues that occurred when using NZ data format with Qwen3-Next models, ensuring correct generation results.

## Technical Significance
NZ format provides memory savings but can introduce precision issues if not handled correctly. The fix ensures Qwen3-Next models can benefit from NZ format memory savings without accuracy degradation. Cherry-picking to v0.11.0 ensures stability for users on that version.

## Related
- `technique-nz-format`, `pattern-accuracy-fix`, `technique-qwen3-next`, `technique-data-format`