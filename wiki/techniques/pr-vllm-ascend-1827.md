---
id: technique-pr-vllm-ascend-1827
title: "PR Insight: vllm-project/vllm-ascend #1827"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - dbo
  - multistream
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1827"
---

# PR Insight: vllm-project/vllm-ascend #1827

**Title:** [BUGFIX][v0.9.1] fix enable_multistream_moe bug when DBO is enabled

## Overview
This PR fixes a bug introduced by code merging that causes issues when both enable_multistream_moe and DBO are enabled. The fix resolves the interaction between these two performance features.

## Technical Significance
Bugfix for feature interaction. Both multistream MoE and DBO are performance optimizations, and their combination requires careful handling to avoid conflicts in expert dispatch and token management.

## Related
- `technique-moe`
- `technique-multistream`
- `technique-dbo`