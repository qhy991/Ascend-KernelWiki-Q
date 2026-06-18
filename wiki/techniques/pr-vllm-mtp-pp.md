---
id: technique-pr-vllm-mtp-pp
title: "PR Insight: MTP + PP Speculative Decoding"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - speculative-decoding
  - pipeline-parallelism
  - deepseek
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10199"
---

# PR Insight: MTP + PP Speculative Decoding

**Source:** [vLLM-Ascend PR #10199](https://github.com/vllm-project/vllm-ascend/pull/10199)

DeepSeek V3 and V4 popularized the **Multi-Token Prediction (MTP)** architecture, a powerful form of speculative decoding where the model natively outputs multiple future tokens per forward pass.

Running MTP on an Ascend cluster becomes exponentially complex when combined with **Pipeline Parallelism (PP)** in a **Prefill-Decode (PD) Disaggregated** scenario.

## The Architectural Challenge

In a typical MTP setup, the final pipeline stage evaluates the predictions and accepts/rejects the speculated tokens. However, in a PD disaggregated setup:
1. One set of NPUs acts as the Prefill worker.
2. Another set acts as the Decode worker.
3. The PP boundary cuts across these nodes.

## The Patch Implementation

The PR introduces specific NPU patches to handle the alignment of model runner outputs when MTP and PP are active simultaneously:
- **Output Alignment**: It synchronizes the hidden states and the MTP module predictions across the HCCS (Huawei Cache Coherent System) links before the KV cache updates are committed to the Unified Buffer.
- **Post-Step Scheduling**: Ascend's execution graph typically requires deterministic tensor shapes. Because speculative decoding acceptance rates are dynamic, the PR handles the dynamic KV cache insertion scheduling *after* the graph execution step, preventing graph recompilation overheads.
