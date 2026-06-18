---
id: technique-pr-vllm-ascend-3643
title: "PR Insight: vllm-project/vllm-ascend #3643"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - mla
  - metadata
  - profiling
  - aclgraph
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3643"
---

# PR Insight: vllm-project/vllm-ascend #3643

**Title:** [v0.11.0][Fix] Fix attention metadata handling for profiling and MLA (#3636)

## Overview
This is a port of PR #3636 to the v0.11.0 branch, fixing attention metadata handling for both profiling and MLA. It moves dummy attention metadata creation to occur after ACL graph runtime mode determination and removes the `attn_metadata` existence check before updating MLA parameters to ensure correct parameter initialization.

## Technical Significance
Backporting critical metadata fixes to release branches ensures users don't encounter profiling failures or incorrect MLA parameter settings. Proper metadata initialization with the correct runtime mode configuration is fundamental to correct attention computation and kernel selection.

## Related
- `technique-attention`
- `technique-mla`
- `technique-aclgraph`