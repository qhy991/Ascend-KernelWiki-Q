---
id: technique-pr-vllm-ascend-5039
title: "PR Insight: vllm-project/vllm-ascend #5039"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - aclgraph
  - testing
  - correctness
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5039"
---

# PR Insight: vllm-project/vllm-ascend #5039

**Title:** [Fix]Revert temporary skip on mtp1/mtp2 correctness tests (aclgraph fix)

## Overview
This PR re-enables MTP1 and MTP2 correctness tests (test_mtp1_correctness_piecewise_graph and test_mtp2_correctness_piecewise_graph) that were temporarily skipped due to an MTP ACL Graph issue. Since the relevant bug has been resolved, these tests are now restored.

## Technical Significance
Restores test coverage for MTP speculative decoding with ACL graph compilation, ensuring correctness across different MTP configurations.

## Related
- `technique-mtp`
- `technique-aclgraph`
- `kernel-mtp-proposer`