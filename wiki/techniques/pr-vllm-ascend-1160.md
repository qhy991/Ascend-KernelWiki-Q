---
id: technique-pr-vllm-ascend-1160
title: "PR Insight: vllm-project/vllm-ascend #1160"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/1160"
---

# PR Insight: vllm-project/vllm-ascend #1160

**Title:** fix torchair execute issue on padding data, and mtp padding logic

## Overview
This PR fixes a torchair execution issue with padding data by deferring padding logic until after multimodal processing. The previous implementation in PR #736 selected valid tokens inside `input_ids` and `position_ids`, which broke the necessary padding requirements for torchair execution.

## Technical Significance
This fix ensures proper handling of padded sequences in torchair graph mode, which is critical for multimodal and variable-length inference scenarios. By postponing the padding logic, the PR maintains torchair's execution requirements while still correctly processing valid tokens in multimodal contexts.

## Related
- `technique-mla`
- `technique-torchair`
- `technique-multimodal`