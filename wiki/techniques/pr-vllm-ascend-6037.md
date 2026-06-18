---
id: technique-pr-vllm-ascend-6037
title: "PR Insight: vllm-project/vllm-ascend #6037"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pcp
  - aclgraph
  - fia
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6037"
---

# PR Insight: vllm-project/vllm-ascend #6037

**Title:** [Bugfix] fix pcp qwen full graph FIA bug

## Overview
This PR fixes an inconsistency between the Q tensor shape and actual q_len in the FIA (Fused In-place Attention) operator for PCP full graph Qwen models. The shape mismatch caused incorrect behavior in graph mode with context parallel.

## Technical Significance
In PCP full graph scenarios with Qwen models, the FIA operator requires the Q tensor shape to match the actual query length. The mismatch occurred during graph capture, leading to incorrect FIA kernel configuration. The fix ensures proper shape handling in acl_graph.py for PCP deployments, enabling correct FIA operator execution with full graph mode.

## Related
- `technique-pcp`, `technique-aclgraph`, `technique-fia`, `technique-qwen`