---
id: technique-pr-vllm-ascend-2706
title: "PR Insight: vllm-project/vllm-ascend #2706"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - refactoring
  - optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2706"
---

# PR Insight: vllm-project/vllm-ascend #2706

**Title:** [main] [refactor] refactor common_fused_moe.py

## Overview
This PR refactors the MoE codebase by moving prepare/finalize operations to a dedicated module, adapting to the token dispatcher interface, and reorganizing the directory structure. The changes improve code organization and maintainability of the fused MoE implementation.

## Technical Significance
Better code organization improves maintainability and makes it easier to optimize and extend MoE functionality. The separation of concerns allows for more targeted optimizations of individual components like prepare/finalize operations and token dispatching.

## Related
- `kernel-fused-moe`
- `technique-moe`
- `technique-refactoring`
- `kernel-token-dispatcher`