---
id: technique-pr-vllm-ascend-5380
title: "PR Insight: vllm-project/vllm-ascend #5380"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mtp
  - rejection-sampling
  - revert
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5380"
---

# PR Insight: vllm-project/vllm-ascend #5380

**Title:** Revert "Add MagicMTP(block verify) and Triton optimization (#4443)"

## Overview
This PR reverts changes from PR #4443 due to precision issues introduced in scenarios where MTP >= 3. The revert restores the previous implementation to maintain numerical correctness.

## Technical Significance
Precision issues in MTP can cause incorrect token predictions and degraded model quality. Reverting problematic optimizations ensures correctness while allowing time to develop a proper fix for the precision issue.

## Related
- technique-mtp
- technique-rejection-sampling
- technique-precision