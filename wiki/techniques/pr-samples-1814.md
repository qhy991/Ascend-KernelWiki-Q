---
id: technique-pr-samples-1814
title: "PR Insight: Ascend/samples #1814"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - venc
  - dvpp
  - samples
  - configuration
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1814"
---

# PR Insight: Ascend/samples #1814

**Title:** Dvpp Venc Sample增加显示帧率用户配置接口

## Overview
This PR adds a user-configurable interface for displaying frame rate in the DVPP VENC sample, allowing developers to monitor and control video encoding performance.

## Technical Significance
Frame rate monitoring is critical for real-time video applications, enabling developers to track encoding throughput and identify performance bottlenecks. Configurable interfaces make samples more practical for production use cases where performance visibility is required.

## Related
- `hw-dvpp`
- `wiki-technique-video-processing`