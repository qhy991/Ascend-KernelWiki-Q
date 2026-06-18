---
id: technique-pr-samples-1450
title: "PR Insight: Ascend/samples #1450"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - pytorch
  - tensorflow
  - channel-sparsity
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1450"
---

# PR Insight: Ascend/samples #1450

**Title:** amct_pytorch&amct_tf 自动通道稀疏sample

## Overview
This PR adds samples for automatic channel sparsity using AMCT for both PyTorch and TensorFlow frameworks. The samples demonstrate the end-to-end workflow for channel pruning and model compression using AMCT on Ascend hardware.

## Technical Significance
Providing samples for both major frameworks is important for developer adoption. These samples show how to apply channel sparsity across different deep learning frameworks while targeting Ascend accelerators.

## Related
- technique-model-compression
- technique-sparsity
- technique-quantization