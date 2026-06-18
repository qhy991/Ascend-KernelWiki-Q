---
id: technique-pr-mindspeed-2206
title: "PR Insight: Ascend/MindSpeed #2206"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - compression
  - training
  - dense
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2206"
---

# PR Insight: Ascend/MindSpeed #2206

**Title:** feat: dense层激活值压缩 -core_r0.10.0

## Overview
This PR adds activation value compression for dense (fully-connected) layers in MindSpeed, targeting the core_r0.10.0 release. The feature compresses activation tensors to reduce memory footprint and communication overhead during distributed training.

## Technical Significance
Dense layer activation compression is a critical optimization for distributed training, particularly for pipeline parallel and tensor parallel training scenarios. By compressing activations, this feature reduces memory bandwidth pressure on HCCL (Huawei Collective Communication Library) and enables training of larger models or larger batch sizes on Ascend NPUs. This optimization is especially important for MoE (Mixture of Experts) models where dense layer activations are frequently communicated across devices.

## Related
- `technique-hccl-optimization`
- `technique-format-conversion`