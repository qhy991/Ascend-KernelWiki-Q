---
id: technique-pr-vllm-ascend-4963
title: "PR Insight: vllm-project/vllm-ascend #4963"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - async-scheduling
  - aclgraph
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4963"
---

# PR Insight: vllm-project/vllm-ascend #4963

**Title:** [Fix] Fixes issues in MTP with async scheduling and ACL graph

## Overview
This PR fixes issues in MTP when async scheduling and full ACL graph mode are both enabled: (1) corrects attention metadata size to prevent mismatches, (2) improves robustness of calculating token sample indices by explicitly aligning tensor shapes, and (3) prevents padding when input tokens exceed max ACL graph batch size to avoid out-of-bounds errors.

## Technical Significance
Resolves multiple correctness issues when combining MTP speculative decoding with async scheduling and ACL graph compilation. Ensures proper tensor shape handling and prevents buffer overflows in edge cases with large batch sizes.

## Related
- `technique-mtp`
- `technique-async-scheduling`
- `technique-aclgraph`
- `kernel-attention-metadata`