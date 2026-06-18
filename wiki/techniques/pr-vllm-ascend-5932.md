---
id: technique-pr-vllm-ascend-5932
title: "PR Insight: vllm-project/vllm-ascend #5932"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - dispatch-gmm
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5932"
---

# PR Insight: vllm-project/vllm-ascend #5932

**Title:** [BugFix] Fix input parameter bug of dispatch_gmm_combine_decode[RFC: issue 5476]

## Overview
This PR fixes a bug where dispatch_gmm_combine_decode was configured with an incorrect global_bs parameter introduced in PR #5040. The parameter should match moe_distributed_dispatch but incorrectly used max_num_tokens instead of properly accounting for tensor parallelism.

## Technical Significance
The global_bs parameter must equal (max batch size across all cards) * (expert parallel world size) to match the moe_distributed_dispatch operator. Using max_num_tokens (which doesn't account for tensor parallelism) resulted in an overestimated value that could cause memory allocation issues or incorrect behavior. The fix corrects the parameter calculation, ensuring proper operator configuration for EPLB scenarios with tensor parallelism.

## Related
- `technique-moe-dispatch`, `technique-eplb`, `technique-tensor-parallel`