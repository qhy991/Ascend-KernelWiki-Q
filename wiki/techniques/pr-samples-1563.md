---
id: technique-pr-samples-1563
title: "PR Insight: Ascend/samples #1563"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - jpegd
  - vpc
  - jpege
  - pipeline
  - hardware-acceleration
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1563"
---

# PR Insight: Ascend/samples #1563

**Title:** jpegd-vpc-jpege串联样例代码

## Overview
This PR adds sample code demonstrating a three-stage DVPP pipeline: JPEG decode (jpegd), vision processing (VPC), and JPEG encode (jpege), forming a complete image processing workflow in hardware.

## Technical Significance
This is a canonical example of DVPP operator chaining showing how to process images entirely in hardware buffers without CPU intervention. The sample teaches buffer handoff between operators, format conversions (e.g., YUV to RGB), resize/crop in VPC, and efficient pipeline scheduling for maximum throughput.

## Related
- `technique-dvpp`
- `technique-pipeline-scheduling`
- `technique-double-buffering`
- `technique-format-conversion`
- `hw-unified-buffer`
- `kernel-jpegd`