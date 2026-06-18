---
id: technique-pr-vllm-ascend-6459
title: "PR Insight: vllm-project/vllm-ascend #6459"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - revert
  - spec-decode
  - inference
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6459"
---

# PR Insight: vllm-project/vllm-ascend #6459

**Title:** [ModelRunner] Revert "[Fix] Pads query_start_loc to satisfy FIA/TND constraint

## Overview
This PR reverts commit 56f5d3bd49ab4275c1bf95d064b020bbf16456fe (from PR #6357) which attempted to pad query_start_loc to satisfy FIA/TND constraints. The revert was necessary because the original fix broke functionality in spec_decode scenarios.

## Technical Significance
Reverts a previous fix that introduced a regression in speculative decoding workflows. The original padding fix for query_start_loc to satisfy FIA/TND constraints caused issues with spec_decode, demonstrating the complexity of balancing different inference modes and kernel constraints.

## Related
- `technique-speculative-decoding`