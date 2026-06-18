---
id: technique-pr-samples-1815
title: "PR Insight: Ascend/samples #1815"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - resize
  - dvpp
  - samples
  - compatibility
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1815"
---

# PR Insight: Ascend/samples #1815

**Title:** Resize 310B适配

## Overview
This PR adapts the DVPP Resize sample for the Ascend 310B processor, ensuring compatibility with the hardware's specific alignment and performance constraints.

## Technical Significance
Processor-specific adaptations are necessary because different Ascend processors have varying DVPP capabilities, memory alignment requirements, and performance characteristics. The 310B optimization ensures developers can use the Resize sample correctly on edge devices with this processor variant.

## Related
- `hw-dvpp`
- `wiki-technique-image-preprocessing`