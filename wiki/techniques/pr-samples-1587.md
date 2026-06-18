---
id: technique-pr-samples-1587
title: "PR Insight: Ascend/samples #1587"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - resnet
  - dvpp
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1587"
---

# PR Insight: Ascend/samples #1587

**Title:** sampleResnetDVPP案例修改

## Overview
This PR further modifies the ResNet DVPP sample code, continuing improvements to the hardware-accelerated preprocessing pipeline for ResNet inference.

## Technical Significance
Iterative sample improvements demonstrate common optimization patterns for DVPP usage. Changes may include better buffer management, improved stride handling for non-aligned images, or enhanced error recovery for edge cases in image preprocessing that affect downstream inference accuracy.

## Related
- `kernel-resnet`
- `technique-dvpp`
- `technique-buffer-management`
- `hw-unified-buffer`