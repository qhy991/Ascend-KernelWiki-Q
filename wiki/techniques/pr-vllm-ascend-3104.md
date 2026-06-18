---
id: technique-pr-vllm-ascend-3104
title: "PR Insight: vllm-project/vllm-ascend #3104"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - terminology
  - refactoring
  - mla
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3104"
---

# PR Insight: vllm-project/vllm-ascend #3104

**Title:** [Refactor] Rename cudagraph_support to aclgraph_support

## Overview
This PR renames the cudagraph_support attribute to aclgraph_support to use terminology appropriate for the Ascend platform (ACL graphs instead of CUDA graphs). It also explicitly disables graph support for the MLA attention backend.

## Technical Significance
Using platform-appropriate terminology improves code clarity and maintainability. Explicitly disabling ACL graph support for MLA backend prevents potential issues with graph capture for MLA attention, which may have compatibility issues with current implementation.

## Related
- `technique-aclgraph`, `kernel-mla-ascendc`, `pattern-terminology-standardization`