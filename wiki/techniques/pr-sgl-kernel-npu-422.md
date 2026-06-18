---
id: technique-pr-sgl-kernel-npu-422
title: "PR Insight: sgl-project/sgl-kernel-npu #422"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mamba
  - state-management
  - prefix-caching
  - mtp
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/422"
---

# PR Insight: sgl-project/sgl-kernel-npu #422

**Title:** adpat move_intermediate_cache for sglang prefix + mtp

## Overview
This PR adapts the move_intermediate_cache function to support sglang's prefix caching combined with MTP (Multi-Token Prediction) functionality. The modifications enable proper state management for Mamba-style attention when both prefix caching and multi-token prediction are enabled.

## Technical Significance
Supporting prefix caching with MTP is essential for efficient inference of long-context models that use Mamba attention with multi-token prediction. The adaptation ensures proper cache management and state transfer between prefix and continuation phases, improving inference efficiency for complex token generation scenarios.

## Related
- `kernel-mamba`, `kernel-state-update`, `technique-prefix-caching`, `technique-multi-token-prediction`