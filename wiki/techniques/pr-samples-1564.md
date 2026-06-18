---
id: technique-pr-samples-1564
title: "PR Insight: Ascend/samples #1564"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - vdec
  - vpc
  - pipeline
  - hardware-acceleration
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1564"
---

# PR Insight: Ascend/samples #1564

**Title:** 增加vdec+vpc串联业务sample

## Overview
This PR adds a sample demonstrating the chained use of VDEC (video decode) and VPC (vision processing center) operators, showing how to build a hardware-accelerated video processing pipeline.

## Technical Significance
Chaining DVPP operators (VDEC for video decode, VPC for image processing) is essential for high-throughput video inference applications. This sample demonstrates buffer management between operators, stream synchronization, and how to maintain data locality in hardware buffers to avoid costly device-host transfers.

## Related
- `technique-dvpp`
- `technique-pipeline-scheduling`
- `technique-operator-chaining`
- `hw-unified-buffer`
- `kernel-vdec`