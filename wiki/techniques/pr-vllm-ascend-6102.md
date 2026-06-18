---
id: technique-pr-vllm-ascend-6102
title: "PR Insight: vllm-project/vllm-ascend #6102"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - spec-decode
  - aclgraph
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6102"
---

# PR Insight: vllm-project/vllm-ascend #6102

**Title:** [0.13.0][Bugfix] Remove `use_aclgraph` in mtp_proposer and use `use_cuda_graph`

## Overview
This is a cherry-pick of PR #6032 for the v0.13.0 release branch. It removes `use_aclgraph` from mtp_proposer and uses `use_cuda_graph` instead, matching the pattern in eagle_proposer.

## Technical Significance
This fix ensures the v0.13.0 branch maintains correctness for MTP with async scheduling. The cherry-pick applies the same logic: properly updating `common_attn_metadata.num_input_tokens = num_input_tokens` after padding, allowing safe use of `use_cuda_graph` instead of the problematic `use_aclgraph` approach.

## Related
- `technique-pr-vllm-ascend-6032`, `technique-mtp`, `technique-spec-decode`, `technique-aclgraph`