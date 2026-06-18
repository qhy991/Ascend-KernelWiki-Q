---
id: technique-pr-samples-2695
title: "PR Insight: Ascend/samples #2695"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - pyacl
  - inference
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2695"
---

# PR Insight: Ascend/samples #2695

**Title:** 新增pyACL快速入门样例 resnet50_firstapp

## Overview
This PR adds a pyACL (Python ACL) quick start sample using ResNet50 as the first application example. The sample provides a complete end-to-end workflow for developers getting started with pyACL for model inference on Ascend hardware.

## Technical Significance
Quick start samples are crucial for onboarding developers to the Ascend ecosystem. The ResNet50 example demonstrates key concepts like model loading, input/output preparation, and inference execution using the pyACL API, providing a clear entry point for new users.

## Related
- `technique-pipeline-scheduling`
- `hw-instruction-queue`