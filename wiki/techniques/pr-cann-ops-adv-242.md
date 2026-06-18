---
id: technique-pr-cann-ops-adv-242
title: "PR Insight: cann-ops-adv #242"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - communication
  - tensor-parallel
  - rmsnorm
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/242"
---

# PR Insight: cann-ops-adv #242 - add matmul_all_reduce_add_rms_norm

## Overview
This PR adds the matmul_all_reduce_add_rms_norm operator, which fuses matrix multiplication, AllReduce, element-wise addition, and RMS Normalization for efficient tensor parallel inference on Ascend NPUs.

## Technical Significance
Fusing four operations (matmul, AllReduce, add, RMS Norm) into a single kernel drastically reduces memory bandwidth and kernel launch overhead. This operator is critical for efficient distributed LLM inference, enabling end-to-end optimized tensor parallel execution.

## Related
- `kernel-matmul`
- `kernel-rmsnorm`
- `technique-tensor-parallel-overlap`
- `technique-operator-fusion`