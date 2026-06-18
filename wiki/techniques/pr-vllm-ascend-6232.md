---
id: technique-pr-vllm-ascend-6232
title: "PR Insight: vllm-project/vllm-ascend #6232"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - eagle
  - acl-graph
  - spec-decode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6232"
---

# PR Insight: vllm-project/vllm-ascend #6232

**Title:** [Bugfix] Add missing draft_attn_metadatas parameter to fix MTP test

## Overview
This PR fixes MTP (Multi-Token Prediction) test failures caused by incorrectly accessing `forward_context.draft_attn_metadatas` which doesn't exist. The fix adds the `draft_attn_metadatas` parameter to the entire call chain in ACL graph compilation, attention backends, and the eagle proposer.

## Technical Significance
The ForwardContext class doesn't include draft_attn_metadatas as an attribute, but the ACL graph update path attempted to access it. The fix ensures draft attention metadata is passed explicitly as function parameters throughout the compilation and attention backend update chain, maintaining API consistency across all attention implementations (V1, CP, MLA).

## Related
- `technique-mtp`, `technique-eagle`, `technique-acl-graph`, `technique-attention`, `technique-mla`