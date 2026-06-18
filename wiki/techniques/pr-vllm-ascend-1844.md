---
id: technique-pr-vllm-ascend-1844
title: "PR Insight: vllm-project/vllm-ascend #1844"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - chunked-prefill
  - torchair
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1844"
---

# PR Insight: vllm-project/vllm-ascend #1844

**Title:** [BugFix] Fix a bug of running chunked-prefill with torchair. (#1378)

## Overview
This PR fixes a bug where the local variable 'decode_hs_or_q_c' was referenced before assignment when running chunked-prefill with torchair. The fix ensures the variable is calculated regardless of whether torchair graph mode is enabled.

## Technical Significance
Critical bugfix for chunked-prefill with torchair. The variable reference bug caused runtime failures when mixing eager prefill with graph decode, a common pattern in production serving.

## Related
- `technique-chunked-prefill`
- `technique-torchair-graph`
- `technique-graph-eager-hybrid`