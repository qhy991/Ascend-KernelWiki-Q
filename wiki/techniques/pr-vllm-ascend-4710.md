---
id: technique-pr-vllm-ascend-4710
title: "PR Insight: vllm-project/vllm-ascend #4710"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - mtp
  - eagle
  - spec-decoding
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4710"
---

# PR Insight: vllm-project/vllm-ascend #4710

**Title:** [Bugfix] fix mtp and eagle aclgraph bug

## Overview
This PR fixes bugs in the ACL graph implementation for MTP (Multi-Token Prediction) and Eagle speculative decoding. The changes affect the spec_decode/eagle_proposer.py and spec_decode/mtp_proposer.py files in the vllm_ascend module.

## Technical Significance
Fixes ACL graph bugs in speculative decoding components (Eagle and MTP) that could cause incorrect graph compilation or execution issues during inference. Ensures correct operator graph generation for these acceleration techniques.

## Related
- `technique-speculative-decoding`
- `technique-aclgraph`
- `kernel-mtp-proposer`
- `kernel-eagle-proposer`