---
id: technique-pr-samples-1933
title: "PR Insight: Ascend/samples #1933"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
  - ascend310p
tags:
  - samples
  - inference
  - 310p
  - compatibility
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1933"
---

# PR Insight: Ascend/samples #1933

**Title:** 部分样例适配310B

## Overview
This PR adapts selected sample code to work with the Ascend310B processor. The adaptations include changes to device detection, memory allocation, and operator invocation to ensure compatibility with the 310B's feature set and capabilities, which differ from the Ascend910/910B training chips.

## Technical Significance
Ascend310B is an inference-focused chip with different hardware characteristics than the 910 series. Adapter modifications ensure sample code works across the Ascend product family, demonstrating how to handle platform-specific features like memory hierarchy, operator availability, and compute capabilities when targeting edge inference scenarios.

## Related
- `hw-platform-compatibility`
- `technique-inference-optimization`