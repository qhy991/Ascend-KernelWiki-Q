---
id: technique-pr-mindspeed-2703
title: "PR Insight: Ascend/MindSpeed #2703"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - performance
  - operator-fusion
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2703"
---

# PR Insight: Ascend/MindSpeed #2703

**Title:** perf: fused_moe_permute

## Overview
This PR implements a fused operator for MoE (Mixture of Experts) token permutation operations in MindSpeed. The `fused_moe_permute` implementation combines token routing permutation operations into a single optimized kernel, reducing memory bandwidth and improving throughput for MoE workloads. The fusion targets the critical path of expert selection and token dispatch in transformer MoE layers.

## Technical Significance
MoE token permutation is a memory-bound operation that can become a bottleneck during expert selection and token routing. By fusing the permutation operations, this optimization reduces intermediate memory transfers and enables better utilization of Ascend's unified-buffer and vector units. This is particularly valuable for large-scale distributed training where MoE expert parallelism is used.

## Related
- `kernel-moe`
- `technique-operator-fusion`
- `technique-nz-tiling`