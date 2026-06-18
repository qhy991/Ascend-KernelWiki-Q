---
id: technique-pr-vllm-ascend-5692
title: "PR Insight: vllm-project/vllm-ascend #5692"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - eagle
  - pcp
  - aclgraph
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5692"
---

# PR Insight: vllm-project/vllm-ascend #5692

**Title:** [main][bugfix] Fix fullgraph padding bug in mtp eagle refactor

## Overview
This PR fixes a padding bug in fullgraph overlay when using MTP and PCP together. The condition for determining padding was modified to accommodate corner cases where the shape capture size is smaller than expected.

## Technical Significance
Bug fix for fullgraph compilation when MTP, EAGLE, and PCP are used together. Proper padding handling is critical for graph compilation correctness, especially with variable sequence lengths and different spec-decode strategies. This fix ensures correct behavior in complex multi-feature scenarios.

## Related
- `technique-spec-decode`, `technique-mtp`, `technique-pcp`