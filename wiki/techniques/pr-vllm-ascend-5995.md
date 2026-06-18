---
id: technique-pr-vllm-ascend-5995
title: "PR Insight: vllm-project/vllm-ascend #5995"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pcp
  - mtp
  - async-scheduling
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5995"
---

# PR Insight: vllm-project/vllm-ascend #5995

**Title:** [0.13.0][Bugfix] fix bug of pcp+mtp+async scheduler

## Overview
This is a cherry-pick of PR #5994 for the v0.13.0 release branch. It fixes the same service suspension issue when PCP, MTP, and async scheduling are enabled together due to shape mismatches after curl requests.

## Technical Significance
This fix ensures the v0.13.0 branch maintains robustness for the PCP+MTP+async scheduling combination. The cherry-pick applies the same tensor shape handling fix to prevent service hangs. This enables reliable deployment scenarios combining all three features on the v0.13.0 release branch.

## Related
- `technique-pr-vllm-ascend-5994`, `technique-pcp`, `technique-mtp`