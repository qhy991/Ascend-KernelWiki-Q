---
id: technique-pr-modellink-2736
title: "PR Insight: Ascend/ModelLink #2736"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - lora
  - moe
  - communication
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2736"
---

# PR Insight: Ascend/ModelLink #2736

**Title:** lora-gemm noneed moe-alltoall-overlap-comm

## Overview
This PR optimizes the interaction between LoRA-GEMM operations and MoE all-to-all communication. It removes unnecessary overlap between these operations when they are not beneficial, improving overall efficiency.

## Technical Significance
MoE models require all-to-all communication for expert routing. Optimizing when and how this overlaps with LoRA-GEMM operations reduces communication overhead and improves training throughput on Ascend NPUs by avoiding unnecessary synchronization.

## Related
- technique-hccl-optimization
- kernel-matmul