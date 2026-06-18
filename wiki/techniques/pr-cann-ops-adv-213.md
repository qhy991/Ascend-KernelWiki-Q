---
id: technique-pr-cann-ops-adv-213
title: "PR Insight: cann-ops-adv #213"
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
  - "https://gitee.com/ascend/cann-ops-adv/pulls/213"
---

# PR Insight: cann-ops-adv #213 - matmulReduceScatter算子开源

## Overview
This PR open-sources the matmulReduceScatter operator, which fuses matrix multiplication with ReduceScatter for efficient tensor parallel inference on Ascend NPUs.

## Technical Significance
Fusing matmul with ReduceScatter reduces synchronization overhead and improves tensor parallel efficiency. This operator is critical for distributed LLM inference, enabling overlapping communication and computation to maximize Ascend hardware utilization.

## Related
- `kernel-matmul`
- `technique-tensor-parallel-overlap`
- `technique-hccl-optimization`
- `hw-hccs`