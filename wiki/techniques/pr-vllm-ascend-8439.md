---
id: technique-pr-vllm-ascend-8439
title: "PR Insight: vllm-project/vllm-ascend #8439"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ffn
  - fusion
  - dispatch-ffn-combine
  - revert
  - combinev2
  - rollback
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8439"
---

# PR Insight: vllm-project/vllm-ascend #8439

**Title:** Revert "[0.18.0][BugFix] dispatch_ffn_combine kernal rollback combinev2 part …"

## Overview
This PR reverts the previous rollback of combinev2 optimization in dispatch_ffn_combine kernel from #8405. The revert restores the combinev2 implementation in csrc/dispatch_ffn_combine/op_kernel/dispatch_ffn_combine_kernel.hpp. The decision indicates that further evaluation showed the original optimization was appropriate or that alternative fixes were found.

## Technical Significance
Reverting a rollback demonstrates the iterative nature of performance optimization and the importance of thorough evaluation. This PR shows that initial performance concerns may be addressed through other means or that the optimization was actually beneficial. The process highlights the need for careful performance analysis and the ability to reverse decisions based on new information.

## Related
- `technique-ffn-optimization`
- `technique-operator-fusion`
- `technique-performance-debugging`