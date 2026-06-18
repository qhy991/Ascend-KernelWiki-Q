---
id: technique-pr-vllm-ascend-8539
title: "PR Insight: vllm-project/vllm-ascend #8539"
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
  - combine
  - unpermute
  - scale
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8539"
---

# PR Insight: vllm-project/vllm-ascend #8539

**Title:** [BugFix] dispatch_ffn_combine kernal rollback combine 、unpermute part and scale part

## Overview
This PR rolls back three optimization points for the decode scenario in the dispatch_ffn_combine kernel based on end-to-end network testing results. The rollback affects combine, unpermute, and scale operations in the kernel implementation to restore stable performance after testing revealed issues with the previous optimizations.

## Technical Significance
This rollback demonstrates the importance of comprehensive end-to-end testing before deploying kernel optimizations. While individual kernel optimizations may show improvements in isolation, they can cause regressions in real-world deployment scenarios. The PR shows a pragmatic approach to performance optimization, prioritizing stability over experimental gains.

## Related
- `technique-ffn-optimization`
- `technique-operator-fusion`
- `technique-performance-debugging`