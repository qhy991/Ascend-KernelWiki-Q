---
id: technique-pr-vllm-ascend-9085
title: "PR Insight: vllm-project/vllm-ascend #9085"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - upgrade
  - cann
  - triton-ascend
  - dependencies
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9085"
---

# PR Insight: vllm-project/vllm-ascend #9085

**Title:** [Misc][Upgrade] Upgrade CANN to 9.0.0 and triton-ascend to 3.2.1

## Overview
This PR upgrades the foundational dependencies for vllm-ascend: CANN (Compute Architecture for Neural Networks) to version 9.0.0 and triton-ascend to version 3.2.1. The upgrade touches CI workflows, Docker files across multiple variants (310p, a2, a3, openEuler), documentation, and version specifications.

## Technical Significance
Upgrading CANN to 9.0.0 and triton-ascend to 3.2.1 provides access to new NPU capabilities, performance optimizations, and bug fixes. This infrastructure upgrade is essential for maintaining compatibility with the latest Ascend hardware features and ensuring optimal performance for kernel operators and attention implementations.

## Related
- `technique-operator-fusion`, `technique-hccl-optimization`