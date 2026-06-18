---
id: technique-pr-vllm-ascend-9692
title: "PR Insight: vllm-project/vllm-ascend #9692"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - expert-selection
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9692"
---

# PR Insight: vllm-project/vllm-ascend #9692

**Title:** [BugFix][MoE] Remove redundant renormalization operations

## Overview
This PR refines expert selection logic in the MoE implementation by eliminating redundant manual weight renormalization and scaling. It updates the expert selection function to use the provided `routed_scaling_factor` instead of hardcoded 1.0 value, and removes manual renormalization and post-fusion scaling steps.

## Technical Significance
Improves code efficiency and maintains consistency with intended routing behavior by correctly passing scaling factors into fusion operations. Removes redundant computational steps that were handled within the fused operation flow, reducing unnecessary computations in MoE expert selection.

## Related
- `technique-moe`, `kernel-matmul`, `pattern-operator-fusion`