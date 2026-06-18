---
id: technique-pr-vllm-ascend-3085
title: "PR Insight: vllm-project/vllm-ascend #3085"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - sequence-parallelism
  - moe
  - aclgraph
  - refactoring
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3085"
---

# PR Insight: vllm-project/vllm-ascend #3085

**Title:** [Refactor] [SP]The sequence parallelism characteristics in the MoE and Dense models are integrated into a single solution.

## Overview
This PR consolidates two sequence parallelism implementations (sequence_parallelism and flashcomm_v1) into a single unified solution for both MoE and Dense models. It removes the sequence_parallelism implementation as it doesn't support ACL Graph, keeping only flashcomm_v1 which is graph-compatible.

## Technical Significance
Unifying sequence parallelism implementations reduces code duplication and maintenance burden. The consolidation ensures ACL Graph compatibility, which is critical for performance optimization on Ascend NPUs. The unified solution provides consistent behavior across MoE and Dense models.

## Related
- `technique-sequence-parallelism`, `kernel-moe-ascendc`, `technique-aclgraph`