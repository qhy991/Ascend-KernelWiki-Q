---
id: technique-pr-vllm-ascend-5679
title: "PR Insight: vllm-project/vllm-ascend #5679"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - sfa
  - dsv3.2
  - spec-decode
  - mtp
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5679"
---

# PR Insight: vllm-project/vllm-ascend #5679

**Title:** [bugfix]support dsv3.2 enable both mtp and full_decode_only

## Overview
This PR fixes a problem introduced in PR #5230 where enabling both mtp and full_decode_only for DSV3.2 model caused operators to fail compilation into the graph. The fix is in the SFA v1 attention implementation.

## Technical Significance
Bug fix for graph compilation in SFA v1 attention when using both MTP and full_decode_only modes. Proper graph compilation is essential for performance in aclgraph mode, and this fix enables correct operator fusion and optimization for DSV3.2 models with spec-decode enabled.

## Related
- `kernel-attention-ascendc`, `technique-sfa`, `technique-spec-decode`