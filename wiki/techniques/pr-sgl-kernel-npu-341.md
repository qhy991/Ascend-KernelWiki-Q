---
id: technique-pr-sgl-kernel-npu-341
title: "PR Insight: sgl-project/sgl-kernel-npu #341"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - gated-delta-rule
  - state-management
  - fla
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/341"
---

# PR Insight: sgl-project/sgl-kernel-npu #341

**Title:** chunk_gated_delta_rule_npu output final state

## Overview
This PR enables final state output in the chunk_gated_delta_rule_npu operator, allowing models to retrieve and use the computed final state for subsequent operations. This enhancement supports recurrent attention patterns where state needs to be propagated across chunks or batches.

## Technical Significance
Outputting final states enables efficient recurrent attention computation for models that maintain state across processing segments. This capability is essential for streaming inference and long-context processing where state must be preserved and reused across multiple forward passes.

## Related
- `kernel-gated-delta-rule`, `kernel-fla-chunk`, `technique-state-management`