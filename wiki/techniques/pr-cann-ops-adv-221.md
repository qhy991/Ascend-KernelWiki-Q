---
id: technique-pr-cann-ops-adv-221
title: "PR Insight: cann-ops-adv #221"
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
  - "https://gitee.com/ascend/cann-ops-adv/pulls/221"
---

# PR Insight: cann-ops-adv #221 - add matmulAllreduce

## Overview
This PR adds the matmulAllreduce operator, which fuses matrix multiplication with AllReduce for efficient tensor parallel training and inference on Ascend NPUs.

## Technical Significance
Fusing matmul with AllReduce reduces synchronization overhead and improves tensor parallel efficiency. This operator is critical for distributed LLM training and inference, enabling overlapping communication and computation to maximize Ascend hardware utilization.

## Related
- `kernel-matmul`
- `technique-tensor-parallel-overlap`
- `technique-hccl-optimization`
- `hw-hccs`