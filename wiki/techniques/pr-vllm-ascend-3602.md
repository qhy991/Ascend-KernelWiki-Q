---
id: technique-pr-vllm-ascend-3602
title: "PR Insight: vllm-project/vllm-ascend #3602"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - torchair
  - logic-unification
  - refactoring
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3602"
---

# PR Insight: vllm-project/vllm-ascend #3602

**Title:** unify logic between aclgraph and torchair

## Overview
This PR continues unifying logic between aclgraph and torchair backends, specifically in the MTP spec decode proposer. The change to `vllm_ascend/spec_decode/mtp_proposer.py` involves a 1-line replacement to ensure consistent behavior across both Ascend compilation backends.

## Technical Significance
Continuing logic unification between aclgraph and torchair reduces code divergence, maintenance burden, and prevents subtle bugs from different implementations. This systematic approach ensures MTP spec decode behaves identically regardless of which Ascend backend is used, improving reliability and simplifying future development.

## Related
- `technique-mtp`
- `technique-spec-decode`
- `technique-aclgraph`