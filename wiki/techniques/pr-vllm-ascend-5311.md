---
id: technique-pr-vllm-ascend-5311
title: "PR Insight: vllm-project/vllm-ascend #5311"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - eplb
  - expert-mapping
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5311"
---

# PR Insight: vllm-project/vllm-ascend #5311

**Title:** [EPLB][refactor] Modification of the initialization logic for expert_map and log2phy（depend on pr5285）

## Overview
This PR refactors EPLB expert map initialization logic to unify handling of expert_map and log2phy across different scenarios. The fix ensures correct expert mapping when redundant experts are enabled and simplifies code in fused_moe by generating maps based on logical expert length.

## Technical Significance
Proper expert mapping is critical for MoE load balancing and token routing. The refactoring fixes bugs where community functions didn't support Ascend's redundant experts and ensures all experts are accessible with correct indexing. The unified logic simplifies maintenance and prevents routing errors.

## Related
- technique-moe
- technique-expert-parallelism
- technique-load-balancing