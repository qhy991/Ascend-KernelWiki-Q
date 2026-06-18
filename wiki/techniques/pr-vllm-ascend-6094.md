---
id: technique-pr-vllm-ascend-6094
title: "PR Insight: vllm-project/vllm-ascend #6094"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - inductor
  - graph-optimization
  - rmsnorm
  - refactor
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6094"
---

# PR Insight: vllm-project/vllm-ascend #6094

**Title:** [Inductor]change pass to adapt to new addrmsnormBias operator

## Overview
This PR modifies the AddRmsNormQuant pass in the Inductor to align with the new addrmsnormBias operator introduced in PR #5790. The change ensures graph optimization passes work correctly with the updated operator.

## Technical Significance
PR #5790 changed the default addrmsnormBias operator when custom ops are enabled. This PR updates the AddRmsNormQuant fusion pass to use the new operator, maintaining graph optimization compatibility. The adaptation ensures that fusion patterns correctly match and optimize with the updated operator, preserving performance benefits of graph optimizations.

## Related
- `technique-inductor`, `technique-rmsnorm`, `technique-graph-optimization`