---
id: technique-pr-mindspeed-chimera-pp
title: "PR Insight: Chimera Bidirectional Pipeline Parallelism"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pipeline-parallelism
  - training
  - mindspeed
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2671"
---

# PR Insight: Chimera Bidirectional Pipeline Parallelism

**Source:** [MindSpeed PR #2671](https://gitee.com/ascend/MindSpeed/pulls/2671)

Pipeline Parallelism (PP) is essential for training models that exceed the memory of a single node (like GPT-4 or DeepSeek V3). However, traditional PP suffers from a massive "bubble"—idle time where NPUs wait for the forward and backward passes to propagate through the entire pipeline.

## The Chimera Architecture

This PR introduces support for **Chimera (Bidirectional Pipeline Parallelism)** natively into the Ascend MindSpeed framework.

Unlike standard 1D PP schedules (like 1F1B or Interleaved 1F1B) which push data in a single direction across the pipeline stages, Chimera effectively deploys two interleaved pipelines:
1. **Pipeline A** pushes micro-batches forward (Stage 0 $\rightarrow$ Stage $N$).
2. **Pipeline B** simultaneously pushes *different* micro-batches backwards (Stage $N \rightarrow$ Stage 0).

## Hardware Impact on Ascend

For the Ascend NPU mesh, this has profound implications:
- **Zero Bubble Limits**: The NPUs are constantly fed with either a forward pass from Pipeline A or a backward pass from Pipeline B, theoretically driving the PP bubble near zero.
- **HCCS Ring Utilization**: Because data is flowing bidirectionally, both the `Tx` (transmit) and `Rx` (receive) lanes of the ultra-high-speed HCCS interconnects are fully saturated, effectively doubling the apparent inter-node network utilization compared to unidirectional 1F1B schedules.
