---
id: technique-pr-cann-ops-adv-355
title: "PR Insight: cann-ops-adv #355"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - documentation
  - moe
  - expert-parallel
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/355"
---

# PR Insight: cann-ops-adv #355 - Add Expert Parallel (EP) Documentation

## Overview
This pull request adds documentation related to the Expert Parallel (EP) capabilities within `cann-ops-adv`. As Mixture of Experts (MoE) architectures become increasingly prevalent in large language models, providing clear and comprehensive developer documentation for distributed expert execution is essential for ecosystem alignment with frameworks like MindSpeed and ModelLink.

## Changes Implemented
- **Documentation Updates**: Added dedicated markdown documentation explaining the mechanics, constraints, and integration of Expert Parallelism within advanced CANN operators.
- **API and Usage Context**: Clarified how relevant operators (e.g., `MoeTokenPermute`, `MoeTokenUnpermute`, `WeightQuantBatchMatmul`) should be configured to correctly partition and dispatch tokens and expert weights across multiple NPU devices.

## Technical Context
In MoE architectures, **Expert Parallel (EP)** distributes different "experts" (sub-networks) across multiple devices in a cluster. Instead of replicating all experts on all NPUs, each NPU only holds a subset. When tokens are processed, they must be dynamically routed over the network (often via All-to-All communication) to the specific NPU hosting the relevant expert.

Within the Huawei Ascend ecosystem:
1. **Operator Support**: The `cann-ops-adv` repository provides fused kernels designed to minimize the overhead of token routing, sorting, and permutation.
2. **Framework Alignment**: High-level frameworks (vLLM-Ascend, MindSpeed) rely on these underlying CANN operators to build the full EP workflow. Proper documentation ensures that developers understand the expected tensor shapes, communication primitives, and memory layout required by the CANN kernels.

## Impact
- **Category**: Documentation & Developer Experience.
- **Severity/Risk**: None.
- **Maintainability**: High. Adding explicit documentation for EP usage prevents misconfigurations in downstream integrations and lowers the barrier to entry for developers optimizing MoE models on Ascend hardware.
