---
id: technique-pr-vllm-ascend-9138
title: "PR Insight: vllm-project/vllm-ascend #9138"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - upgrade
  - torch-npu
  - cann
  - triton-ascend
  - dependencies
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9138"
---

# PR Insight: vllm-project/vllm-ascend #9138

**Title:** [Misc] upgraph torch_npu, cann and triton-ascend

## Overview
This PR upgrades the core dependencies: torch_npu to version 2.9.0.post2, CANN to 9.0.0, and triton-ascend to 3.2.1. The upgrade affects CI workflows, Docker files across multiple variants (310p, a2, a3, openEuler), documentation, and version specifications throughout the codebase.

## Technical Significance
The coordinated upgrade of torch_npu, CANN, and triton-ascend ensures compatibility and access to the latest NPU capabilities, performance optimizations, and bug fixes. This infrastructure upgrade is essential for maintaining support for current Ascend hardware features and enabling optimal performance for kernel operators and attention implementations across the vllm-ascend stack.

## Related
- `kernel-attention-ascendc`, `technique-operator-fusion`, `technique-hccl-optimization`