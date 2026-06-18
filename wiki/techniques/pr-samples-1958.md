---
id: technique-pr-samples-1958
title: "PR Insight: Ascend/samples #1958"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - distillation
  - mobilenet
  - v2
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1958"
---

# PR Insight: Ascend/samples #1958

**Title:** Add mobilenet v2 distill sample

## Overview
This PR adds a new sample demonstrating knowledge distillation for MobileNetV2. The sample shows how to compress a MobileNetV2 model using distillation techniques for deployment on Ascend hardware.

## Technical Significance
Knowledge distillation transfers knowledge from a large teacher model to a smaller student model, reducing size and inference latency. This sample demonstrates practical distillation workflows for mobile-friendly models like MobileNetV2, which is important for edge deployment on Ascend310P inference cards.

## Related
- `technique-ascendc`