---
id: technique-pr-vllm-ascend-3630
title: "PR Insight: vllm-project/vllm-ascend #3630"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - aclgraph
  - batch-size
  - performance
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3630"
---

# PR Insight: vllm-project/vllm-ascend #3630

**Title:** [v0.11.0] cherry-pick Fix performance degradation when mtp>1 (#3597)

## Overview
This is a cherry-pick of PR #3597 to the v0.11.0 branch, fixing performance degradation when MTP count exceeds 1. The issue occurs because larger batch sizes exceed aclgraph's maximum batch size limit, forcing the draft model into eager mode. The fix was implemented in `vllm_ascend/utils.py` with 20 lines of new logic.

## Technical Significance
Cherry-picking critical fixes to release branches ensures users get performance and stability improvements. This backport prevents v0.11.0 users from experiencing eager mode fallback penalties when using MTP>1, maintaining optimal inference throughput for draft model execution.

## Related
- `technique-mtp`
- `technique-aclgraph`
- `technique-batch-optimization`