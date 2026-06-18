---
id: technique-pr-vllm-ascend-5931
title: "PR Insight: vllm-project/vllm-ascend #5931"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - dispatch-gmm
  - bugfix
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5931"
---

# PR Insight: vllm-project/vllm-ascend #5931

**Title:** [v0.13.0][BugFix][Cherry Pick] Fix input parameter bug of dispatch_gmm_combine_decode

## Overview
This is a cherry-pick of PR #5932 for the v0.13.0 release branch. It fixes a bug where dispatch_gmm_combine_decode was configured with an incorrect global_bs parameter that didn't account for tensor parallelism.

## Technical Significance
The global_bs parameter should equal (max batch size across all cards) * (expert parallel world size), matching the moe_distributed_dispatch operator. However, the implementation incorrectly used max_num_tokens, which doesn't account for tensor parallelism, resulting in an overestimated value. The fix ensures correct parameter configuration for the dispatch_gmm_combine_decode operator, maintaining accuracy for EPLB scenarios.

## Related
- `technique-pr-vllm-ascend-5932`, `technique-moe-dispatch`, `technique-eplb`