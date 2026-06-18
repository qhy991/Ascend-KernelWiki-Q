---
id: technique-pr-vllm-ascend-5817
title: "PR Insight: vllm-project/vllm-ascend #5817"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eplb
  - moe
  - expert-parallel
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5817"
---

# PR Insight: vllm-project/vllm-ascend #5817

**Title:** [EPLB][Bugfix] Get expert map from layers

## Overview
This PR fixes inconsistent expert_map initialization between the EPLB module and the fused_moe module. The EPLB module was using a different initialization method that led to incorrect expert mapping. The fix removes the EPLB-specific initialization and makes both modules use the same consistent expert_map from the layers.

## Technical Significance
Expert mapping is critical for EPLB to correctly route tokens to experts. The inconsistency caused incorrect expert assignments, affecting model accuracy. By ensuring both EPLB and fused_moe use the same expert_map source, the fix eliminates routing errors. Testing on Qwen3-235B-W8A8 with EPLB shows 86.67% accuracy on AIME2024 after the fix. The changes span the EPLB adaptor, utils, and fused_moe implementations.

## Related
- `technique-expert-parallel`, `technique-eplb`, `technique-moe-dispatch`