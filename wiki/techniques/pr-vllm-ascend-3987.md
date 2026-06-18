---
id: technique-pr-vllm-ascend-3987
title: "PR Insight: vllm-project/vllm-ascend #3987"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - paged-attention
  - bugfix
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3987"
---

# PR Insight: vllm-project/vllm-ascend #3987

**Title:** [cherry-pick][v0.11.0-dev][bugfix] Fix a rare bug triggered by _npu_paged_attention in FULL_DECODE_ONLY mode

## Overview
This is a cherry-pick of PR #3986 to the v0.11.0-dev branch, fixing the same bug where `_npu_paged_attention` workspace calculation during graph capture was insufficient for some execution scenarios. The fix adds proper workspace calculation in `update_attn_params` to handle edge cases where smaller seq_lens require larger workspace.

## Technical Significance
Cherry-picking critical bugfixes ensures stability across vLLM versions. The workspace calculation bug is rare but serious, potentially causing crashes in production. The v0.11.0-dev branch fix ensures users on that version get the same correctness guarantees as the main branch, preventing production issues.

## Related
- `technique-attention`, `technique-paged-attention`, `technique-aclgraph`, `pattern-memory-safety`