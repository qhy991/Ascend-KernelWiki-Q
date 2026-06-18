---
id: technique-pr-vllm-ascend-3560
title: "PR Insight: vllm-project/vllm-ascend #3560"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - aclgraph
  - torchair
  - spec-decode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3560"
---

# PR Insight: vllm-project/vllm-ascend #3560

**Title:** unify logic between aclgraph and torchair

## Overview
This PR unifies the logic between aclgraph and torchair backends for MTP (multi-text-prompt) spec decode functionality. The change was made to `vllm_ascend/spec_decode/mtp_proposer.py`, involving a minimal 1-line addition and 1-line deletion to ensure consistent behavior across both Ascend backends.

## Technical Significance
Unifying logic between aclgraph and torchair is critical for MTP spec decode to ensure consistent performance and correctness regardless of which Ascend compilation backend is used. This reduces maintenance burden and prevents subtle bugs from divergent implementations. MTP spec decode is a key optimization technique for accelerating text generation in vLLM.

## Related
- `technique-mtp`
- `technique-spec-decode`
- `technique-aclgraph`