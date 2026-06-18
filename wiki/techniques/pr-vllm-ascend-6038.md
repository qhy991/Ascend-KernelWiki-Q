---
id: technique-pr-vllm-ascend-6038
title: "PR Insight: vllm-project/vllm-ascend #6038"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pcp
  - aclgraph
  - fia
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6038"
---

# PR Insight: vllm-project/vllm-ascend #6038

**Title:** [0.13.0][Bugfix] fix pcp aclgraph qwen FIA bug

## Overview
This is a cherry-pick of PR #6037 for the v0.13.0 release branch. It fixes the same inconsistency between Q tensor shape and actual q_len in the FIA operator for PCP full graph Qwen models.

## Technical Significance
This fix ensures the v0.13.0 branch maintains correctness for PCP full graph scenarios with Qwen models. The cherry-pick applies the same shape handling fix to acl_graph.py, enabling correct FIA operator execution with full graph mode on the release branch.

## Related
- `technique-pr-vllm-ascend-6037`, `technique-pcp`, `technique-aclgraph`, `technique-fia`