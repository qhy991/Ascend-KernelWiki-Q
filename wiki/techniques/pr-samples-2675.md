---
id: technique-pr-samples-2675
title: "PR Insight: Ascend/samples #2675"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - model
  - mobilenet
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2675"
---

# PR Insight: Ascend/samples #2675

**Title:** update mobilenet_v2_1.0_224.tgz download url

## Overview
This PR updates the download URL for the mobilenet_v2_1.0_224.tgz model file. The change ensures samples can successfully fetch the required MobileNetV2 model from the correct location.

## Technical Significance
Keeping model download URLs current is essential for sample reproducibility. MobileNet is a common model for demonstrating inference workflows, and having accessible model files helps developers quickly test and understand the samples.

## Related
- `technique-pipeline-scheduling`
- `kernel-attention-ascendc`