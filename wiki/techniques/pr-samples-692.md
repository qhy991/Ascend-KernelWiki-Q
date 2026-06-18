---
id: technique-pr-samples-692
title: "PR Insight: Ascend/samples #692"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - googlenet
  - image-classification
  - atlas
  - cpp
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/692"
---

# PR Insight: Ascend/samples #692

**Title:** cplusplus/googlenet_imagenet_picture with atlas interface

## Overview
This PR implements a C++ GoogleNet ImageNet picture classification sample using the Atlas interface API. The sample demonstrates how to run GoogleNet on Ascend hardware using the C++ Atlas APIs.

## Technical Significance
Providing C++ Atlas interface samples enables developers to build high-performance applications using the native Ascend APIs. The Atlas interface provides low-level control over Ascend hardware resources, which is important for optimizing performance-critical applications.

## Related
- N/A (Atlas API)