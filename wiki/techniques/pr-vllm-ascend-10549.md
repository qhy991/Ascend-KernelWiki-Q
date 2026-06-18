---
id: technique-pr-vllm-ascend-10549
title: "PR Insight: vllm-ascend #10549"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - acl-graph
  - performance
  - multimodal
  - vision-transformer
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10549"
---

# [Feature] ViT encoder ACL graph

## Overview
PR #10549 in the `vllm-ascend` repository implements an Ascend-specific ACL (Ascend Computing Language) graph capture and replay mechanism tailored for multimodal encoder attention (`MMEncoderAttention`). This enhancement is crucial for optimizing the performance of Vision Transformers (ViT) and other multimodal encoders on Huawei Ascend NPUs.

## Architectural Explanation
In dynamic multimodal architectures, the vision encoder processes inputs of varying shapes (such as multiple images or dynamic resolutions). When deploying models on accelerators, CPU overhead from kernel dispatch can become a significant bottleneck, particularly during the encoder phase.

To address this, the PR implements an **ACL graph capture and replay mechanism**:
1. **ACL Graph**: Similar to CUDA Graphs, ACL graphs allow the system to capture a sequence of NPU operations and replay them without incurring the host-side dispatch overhead for each individual operation.
2. **`MMEncoderAttention` Adaptation**: The multimodal encoder's attention layer is wrapped to support this graph execution mode.
3. **Task Groups for Metadata Binding**: The implementation utilizes task groups to bind host-side metadata during the graph capture phase. This ensures that the dynamic aspects of the encoder execution are correctly captured and managed within the static graph structure.
4. **`npu_fused_infer_attention_score` Integration**: The graph utilizes the Ascend `npu_fused_infer_attention_score` kernel (Fused Infer Attention) to compute the attention scores efficiently within the captured graph, maintaining high throughput for the encoder.

## Impact
By enabling ACL graph capture for `MMEncoderAttention`, the PR drastically reduces the CPU overhead during the vision encoding phase in multimodal large language models (MLLMs). This leads to lower latency and higher end-to-end throughput, especially when processing multiple high-resolution images or utilizing dynamic batching mechanisms.
