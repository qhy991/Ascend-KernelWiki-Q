---
id: technique-pr-vllm-ascend-3163
title: "PR Insight: vllm-project/vllm-ascend #3163"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - shared-expert
  - torch-dynamo
  - accuracy
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3163"
---

# PR Insight: vllm-project/vllm-ascend #3163

**Title:** [BugFix] Fix aclgraph accu problem in A2.

## Overview
This PR fixes accuracy problems in ACL graph mode on A2 hardware. The issue was introduced by PR #2980, which exposed shared_expert all_reduce operations to torch dynamo. The fix moves all affected code into forward_impl to shield it from torch dynamo.

## Technical Significance
Torch dynamo graph capture can interfere with collective communication operations if not properly isolated. Moving shared expert all_reduce into forward_impl prevents incorrect graph capturing and ensures accuracy. This demonstrates the complexity of integrating custom operators with PyTorch's graph compilation.

## Related
- `technique-aclgraph`, `kernel-shared-expert-ascendc`, `pattern-torch-dynamo-integration`