---
id: technique-pr-samples-1953
title: "PR Insight: Ascend/samples #1953"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - resnet
  - dvpp
  - inference
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1953"
---

# PR Insight: Ascend/samples #1953

**Title:** update inference/modelInference/sampleResnetDVPP/python/src/sampleResnetDVPP.py

## Overview
This PR updates the ResNet50 DVPP (Digital Vision Pre-Processing) sample Python implementation. The sample demonstrates using DVPP hardware acceleration for image preprocessing before running ResNet50 inference, leveraging the NPU's dedicated vision processing unit for efficient JPEG decode and resize operations.

## Technical Significance
DVPP is a critical hardware feature on Ascend NPUs that offloads image preprocessing from the CPU to dedicated hardware, significantly improving throughput for vision inference workloads. The ResNet50 DVPP sample shows best practices for combining hardware-accelerated preprocessing with NPU inference, demonstrating efficient data flow from DVPP output directly to NPU compute units.

## Related
- `hw-dvpp`
- `kernel-resnet`
- `technique-data-reuse`