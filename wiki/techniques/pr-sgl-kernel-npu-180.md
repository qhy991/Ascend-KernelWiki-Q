---
id: technique-pr-sgl-kernel-npu-180
title: "PR Insight: sgl-project/sgl-kernel-npu #180"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - aicore
  - detection
  - adaptive
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/180"
---

# PR Insight: sgl-project/sgl-kernel-npu #180

**Title:** Support device with different counts of AICore (FusedDeepMoe operator)

## Overview
Enhances the FusedDeepMoe operator to detect and adapt to devices with different counts of AICore. The operator now dynamically determines the number of available AICore and uses an equivalent number of cores, with testing confirmed for 20 and 24 core configurations.

## Technical Significance
This adaptive AICore detection makes the FusedDeepMoe operator portable across different Ascend device configurations with varying AICore counts. The dynamic core allocation ensures optimal resource utilization regardless of the specific device configuration, improving operator flexibility and deployment compatibility across different Ascend hardware variants.

## Related
- `wiki-kernel-moe`
- `wiki-hardware-aicore`
- `wiki-technique-adaptive-computation`
- `wiki-technique-resource-detection`