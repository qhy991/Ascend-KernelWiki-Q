---
id: technique-pr-vllm-ascend-8534
title: "PR Insight: vllm-project/vllm-ascend #8534"
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
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8534"
---

# PR Insight: vllm-project/vllm-ascend #8534

**Title:** [BugFix][0.18.0]dispatch_ffn_combine kernal rollback combine 、unpermute part and scale part

## Overview
This PR is a cherry-pick of #8539 to the v0.18.0 release branch, rolling back three optimization points for the decode scenario in the dispatch_ffn_combine kernel due to end-to-end network testing results. The rollback affects combine, unpermute, and scale operations in the kernel implementation to restore stable performance.

## Technical Significance
This cherry-pick ensures consistency between main and release branches for dispatch_ffn_combine kernel optimizations. The rollback decisions based on end-to-end testing demonstrate the importance of comprehensive performance validation across different deployment scenarios. Maintaining stability is prioritized over experimental optimizations that may cause issues in production.

## Related
- `technique-ffn-optimization`
- `technique-operator-fusion`
- `technique-performance-debugging`