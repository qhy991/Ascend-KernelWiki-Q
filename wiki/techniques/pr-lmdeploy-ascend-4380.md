---
id: technique-hybrid-parallelism-s1pro
title: "Hybrid 3D Parallelism (DP x TP + EP) for MoE on Ascend"
type: wiki-technique
confidence: verified
architectures:
  - ascend910b
kernel_types:
  - moe
tags:
  - s1-pro
  - expert-parallel
  - tensor-parallel
sources:
  - pr-lmdeploy-ascend-4380
---

# Hybrid 3D Parallelism (DP x TP + EP) for MoE on Ascend

## Context
Deploying massive trillion-parameter MoE architectures (like S1-Pro or DeepSeek-V3) requires advanced sharding techniques. Because MoE models introduce sparsity, standard Tensor Parallelism (TP) becomes inefficient when applied to the MLP/Expert layers, as it forces all NPUs to hold fractions of unused experts.

## DP x TP + EP Strategy
The `DP * TP + EP` strategy optimizes the layout:
- **Attention Layers**: Evaluated using standard **Tensor Parallelism (TP)** inside a single node (e.g., 8x Ascend 910B) to maximize ultra-fast intra-node bandwidth (HCCS).
- **MoE Layers**: Evaluated using **Expert Parallelism (EP)**. Instead of sharding individual experts, entire experts are assigned to specific NPUs across the cluster.
- **Batch Processing**: **Data Parallelism (DP)** handles overall batch scaling.

### HCCL Collective Mechanics
When transitioning from the Attention layer (TP domain) to the MoE layer (EP domain), the activations must be routed to the correct NPU holding the selected expert. This requires an `AllToAll` collective communication via HCCL (Huawei Collective Communication Library). 
The LMDeploy backend orchestrates the HCCL communicators such that the `AllToAll` scatter/gather correctly accounts for the active `DP` and `TP` ranks, ensuring that tokens routed to an expert on a remote node do not collide with local TP reduction streams.
