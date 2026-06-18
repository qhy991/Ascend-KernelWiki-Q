---
id: technique-pr-vllm-ascend-5711
title: "PR Insight: vllm-project/vllm-ascend #5711"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - xlite
  - graph-mode
  - padding
  - decode
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5711"
---

# PR Insight: vllm-project/vllm-ascend #5711

**Title:** [BugFix] Xlite: Bypass the padding of the graph mode in non-MTP cases to obtain the correct decode num.

## Overview
This PR fixes a bug in the Xlite backend where illegal negative token counts were calculated for decode requests due to graph mode padding and cross-step state issues. The problem occurred when new prefill requests were added simultaneously with completed decode requests, causing the `attn_metadata.num_decode` array to be expanded to a threshold (8 tokens) while `self.query_start_loc` tracking became misaligned. The fix uses `num_decode_tokens` instead of `attn_metadata.num_decodes` to bypass the padding mechanism.

## Technical Significance
This bugfix addresses a critical coordination issue between graph mode padding and token tracking across inference steps. The root cause was poor coordination between the padding mechanism that expands decode arrays for graph mode and the `query_start_loc` class variable that tracks tokens. When negative values overflowed during type conversion, Xlite would trigger a "decode len too long" alert. The fix ensures accurate token counting for decode requests by using the actual decoded token count rather than the padded array length.

## Related
- `technique-pipeline-scheduling`, `technique-graph-mode`, `technique-inference`