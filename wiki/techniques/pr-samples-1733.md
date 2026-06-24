---
id: technique-pr-samples-1733
title: "PR Insight: Ascend/samples #1733"
type: wiki-technique
architectures:
  - ascend910
  - ascend310p
tags:
  - samples
  - 310b
  - autonomous-driving
  - porting
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1733"
---

# PR Insight: Ascend/samples #1733

**Title:** 辅助驾驶样例支持310B

## Overview
This PR adapts the autonomous driving (assisted driving) sample to run on the Ascend 310B platform, extending hardware support for this use case.

## Technical Significance
Porting samples to different Ascend hardware platforms (310, 310B, 310P, 910, 910B) helps developers understand architectural differences and porting considerations. Autonomous driving scenarios often require edge deployment on lower-power chips like the 310B.

## Related
- wiki-hardware-ascend310b
- technique-edge-inference