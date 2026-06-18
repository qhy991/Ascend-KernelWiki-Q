---
id: technique-pr-vllm-ascend-3125
title: "PR Insight: vllm-project/vllm-ascend #3125"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - mla
  - decode-only
  - workspace
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3125"
---

# PR Insight: vllm-project/vllm-ascend #3125

**Title:** [Feat][Graph]Support FULL_DECEDE_ONLY mode for MLA models

## Overview
This PR adds support for capturing Multi-Layer Attention (MLA) decode operations into ACL graphs in FULL_DECODE_ONLY mode. It implements graph capture logic for the MLA kernel, including workspace management and parameter updates, with modifications to rotary embedding operations.

## Technical Significance
Compiling MLA attention kernels for single-token decoding improves performance through ACL graph optimization. The workspace management and parameter update handling ensure correct graph execution. This extends ACL graph benefits to MLA models, which are increasingly common in modern architectures.

## Related
- `kernel-mla-ascendc`, `technique-aclgraph`, `pattern-full-decode-only`