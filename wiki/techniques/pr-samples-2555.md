---
id: technique-pr-samples-2555
title: "PR Insight: Ascend/samples #2555"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - dataflow
  - pytorch
  - online-inference
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2555"
---

# PR Insight: Ascend/samples #2555

**Title:** 新增DataFlow结合Pytorch进行模型在线推理的样例

## Overview
This PR adds a sample demonstrating DataFlow combined with PyTorch for online model inference. The example shows how to integrate dataflow programming patterns with PyTorch for efficient online inference on Ascend hardware.

## Technical Significance
Combining DataFlow with PyTorch provides a powerful approach for high-performance online inference. Dataflow enables efficient pipeline execution, while PyTorch provides a familiar deep learning framework interface.

## Related
- `technique-pipeline-scheduling`
- `hw-event-sync`
- `technique-cube-vector-overlap`
- `kernel-attention-ascendc`