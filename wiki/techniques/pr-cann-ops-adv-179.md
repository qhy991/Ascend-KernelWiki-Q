---
id: technique-pr-cann-ops-adv-179
title: "PR Insight: cann-ops-adv #179"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - communication
  - tensor-parallel
  - hccl
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/179"
---

# PR Insight: cann-ops-adv #179 - add allgather_matmul

## Overview
This PR adds the allgather_matmul operator, which fuses HCCL AllReduce with matrix multiplication for efficient tensor parallel inference on Ascend NPUs.

## Technical Significance
Fusing AllReduce with matmul reduces synchronization overhead and improves tensor parallel efficiency. This operator is critical for distributed LLM inference, enabling overlapping communication and computation to maximize Ascend hardware utilization.

## Related
- `kernel-matmul`
- `technique-tensor-parallel-overlap`
- `technique-hccl-optimization`
- `hw-hccs`