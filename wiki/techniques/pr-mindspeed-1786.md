---
id: technique-pr-mindspeed-1786
title: "PR Insight: Ascend/MindSpeed #1786"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - gmm
  - tensor
  - compatibility
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1786"
---

# PR Insight: Ascend/MindSpeed #1786

**Title:** gmm适配grouplist为npu tensor情况

## Overview
This PR adapts GMM (likely Gaussian Mixture Model or general matrix multiplication) to handle cases where grouplist is an NPU tensor. The change improves compatibility with NPU-specific tensor formats.

## Technical Significance
Proper handling of NPU tensors is important for avoiding unnecessary data transfers between host and device. Adapting GMM to work with NPU tensors directly improves performance by reducing data movement overhead on Ascend NPUs.

## Related
- matmul
- tensor-formats
- device-memory management