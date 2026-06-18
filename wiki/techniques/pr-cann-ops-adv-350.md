---
id: technique-pr-cann-ops-adv-350
title: "PR Insight: cann-ops-adv #350"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - communication
  - operators
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/350"
---

# PR Insight: cann-ops-adv #350 (Add dispatch & combine v2)

## Overview
This PR introduces the second generation of Mixture of Experts (MoE) distribution operators in CANN: `MoeDistributeDispatchV2` and `MoeDistributeCombineV2`. These operators provide comprehensive support for routing and combining tokens across experts distributed on different devices, handling complex routing strategies common in advanced large language models (LLMs) such as those featuring Shared Experts (e.g., DeepSeek-V2).

## Architectural Details

### 1. `MoeDistributeDispatchV2`
This operator handles the routing phase of MoE inference, breaking down global input tokens and preparing them for the specific experts located on varying ranks.
- **Inputs:** It takes the un-routed input tokens (`x`), expert routing mapping (`expert_ids`), and scalar routing weights (`expert_scales` or `scales`).
- **Outputs:** Outputs the expanded tokens (`expandX`), dynamic scales, and routing indices, while computing the communication sizes needed for both Expert Parallelism (`ep_recv_counts`) and Tensor Parallelism (`tp_recv_counts`). 
- **Communication:** Integrates deeply with Huawei Collective Communication Library (HCCL), requiring EpComm and TpComm to facilitate correct message passing configuration among Ascend NPUs.

### 2. `MoeDistributeCombineV2`
This operator works symmetrically to DispatchV2 by collecting the outputs from distributed experts and collapsing them back into the original token order.
- **Inputs:** Re-ingests the expanded tokens from experts (`expandX`), token mappings (`expert_ids`), and the previously calculated communication counts (`ep_send_counts`, `tp_send_counts`). It can also optionally intake the output from shared experts (`shared_expert_x`) to fuse them in a single step.
- **Outputs:** Generates the combined tokens matching the original batch shapes.

### Key Enhancements in V2
Compared to earlier versions, the `v2` implementation adds fine-grained control parameters:
- **Shared Experts Handling:** Explicitly accepts `shared_expert_num` and `shared_expert_rank_num` attributes, natively supporting models that bypass routing for a globally shared expert.
- **Quantized Communication:** Supports `comm_quant_mode`, which allows the `expandX` tensor to use `int8` quantization instead of `bf16` during all-to-all communications, substantially reducing communication bottleneck overhead across HCCL links.
- **2D Topologies:** Actively handles both Expert Parallelism (EP) and Tensor Parallelism (TP) simultaneously using dedicated communicator groups (`group_ep` and `group_tp`).

## Conclusion
The addition of `aclnnMoeDistributeDispatchV2` and `aclnnMoeDistributeCombineV2` marks a critical step towards improving CANN's support for modern, large-scale MoE topologies. By fusing shared-expert addition and providing quantization for inter-NPU token dispatching, memory throughput and scaling efficiency will significantly improve on Ascend clusters.
