---
id: technique-pr-vllm-ascend-1214
title: "PR Insight: vllm-project/vllm-ascend #1214"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mla
  - torchair
  - padding
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1214"
---

# PR Insight: vllm-project/vllm-ascend #1214

**Title:** fix torchair execute issue on padding data, and mtp padding logic

## Overview
This is a cherry-pick of PR #1160 to fix torchair execution issues with padding data. The fix defers padding logic until after multimodal processing to maintain torchair's execution requirements while correctly handling valid tokens in multimodal contexts.

## Technical Significance
This backport ensures that the padding fix is available in the appropriate release branch, maintaining consistent behavior across different versions. The fix is critical for multimodal inference scenarios where proper padding handling is essential for torchair graph execution.

## Related
- `technique-mla`
- `technique-torchair`
- `technique-multimodal`