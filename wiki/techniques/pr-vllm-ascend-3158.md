---
id: technique-pr-vllm-ascend-3158
title: "PR Insight: vllm-project/vllm-ascend #3158"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - oom
  - token-dispatch
  - memory-management
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3158"
---

# PR Insight: vllm-project/vllm-ascend #3158

**Title:** [bugfix] fix oom in aclgraph

## Overview
This PR fixes out-of-memory errors in ACL graph mode caused by tensor lifecycle management issues. In the token dispatch implementation, tensors mounted on class instances prevent automatic recycling, leading to OOM in some cases. The fix manually sets these tensors to None to release memory.

## Technical Significance
Proper tensor lifecycle management is critical for ACL graph execution, where graphs may capture and retain tensor references. Manual memory release ensures that intermediate tensors don't accumulate across graph executions, preventing OOM errors in long-running inference sessions.

## Related
- `technique-aclgraph`, `kernel-moe-ascendc`, `technique-memory-management`