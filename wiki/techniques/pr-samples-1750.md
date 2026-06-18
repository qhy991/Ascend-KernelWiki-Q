---
id: technique-pr-samples-1750
title: "PR Insight: Ascend/samples #1750"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deeplabv3
  - multi-thread
  - multi-device
  - samples
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1750"
---

# PR Insight: Ascend/samples #1750

**Title:** 【issue问题处理】解决deeplabv3_multi_thread_multi_device预处理发送数据问题

## Overview
This PR fixes a data transmission issue in the preprocessing stage of the DeepLabV3 multi-thread, multi-device sample.

## Technical Significance
Multi-thread, multi-device inference is critical for scaling inference throughput across multiple Ascend processors. Fixing data transmission issues in the preprocessing pipeline ensures that work can be correctly distributed and synchronized across threads and devices, maximizing hardware utilization.

## Related
- `wiki-technique-inference`
- `wiki-technique-multi-device`