---
id: technique-pr-vllm-ascend-3753
title: "PR Insight: vllm-project/vllm-ascend #3753"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - multistream
  - hccl-optimization
  - aclgraph
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3753"
---

# PR Insight: vllm-project/vllm-ascend #3753

**Title:** [Cherry-pick] Port MoE multi-stream fix to v0.11.0-dev

## Overview
This is a cherry-pick of PR #3582 to the v0.11.0-dev branch, fixing MoE multi-stream issues. The fix moves shared expert communication operations out of the extra stream to prevent rtMemcpy errors in aclgraph mode, and uses a global variable for the extra stream object to avoid per-layer stream allocation in full-graph mode.

## Technical Significance
Backporting critical multi-stream stability fixes prevents rtMemcpy errors in production. Using a global stream object reduces resource allocation overhead in full-graph mode while maintaining the separation of shared expert communication from the extra stream that caused errors.

## Related
- `technique-moe`
- `technique-hccl-optimization`
- `technique-multistream`