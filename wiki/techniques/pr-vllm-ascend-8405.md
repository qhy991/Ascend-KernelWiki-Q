---
id: technique-pr-vllm-ascend-8405
title: "PR Insight: vllm-project/vllm-ascend #8405"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ffn
  - fusion
  - dispatch-ffn-combine
  - bugfix
  - rollback
  - combinev2
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8405"
---

# PR Insight: vllm-project/vllm-ascend #8405

**Title:** [0.18.0][BugFix] dispatch_ffn_combine kernel rollback combinev2 part

## Overview
This PR temporarily rolls back the combinev2 optimization in the dispatch_ffn_combine kernel due to performance degradation in certain scenarios. The rollback affects the kernel implementation in csrc/dispatch_ffn_combine/op_kernel/dispatch_ffn_combine_kernel.hpp. The decision was made after end-to-end testing revealed that the optimization caused performance issues in some cases.

## Technical Significance
Performance rollbacks are sometimes necessary when optimizations reveal unexpected negative impacts in real-world scenarios. This PR demonstrates the importance of comprehensive end-to-end testing before deploying kernel optimizations. The rollback maintains system stability while allowing for further investigation into the performance regression root cause.

## Related
- `technique-ffn-optimization`
- `technique-operator-fusion`
- `technique-performance-debugging`