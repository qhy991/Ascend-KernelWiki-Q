---
id: technique-pr-samples-1481
title: "PR Insight: Ascend/samples #1481"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - presenter-server
  - web-ui
  - video-processing
  - screen-recording
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1481"
---

# PR Insight: Ascend/samples #1481

**Title:** presenterserver web页面增加截图（获取当前图片）和录屏（保存一段视频）保存到本地

## Overview
This PR adds screenshot (capture current image) and screen recording (save video segment) functionality to the presenter server web interface, saving files locally.

## Technical Significance
Presenter server provides web-based visualization for inference results. Adding screenshot and recording capabilities improves debugging and demonstration workflows, allowing developers to capture and share inference pipeline behavior, video analytics results, or system performance visualization.

## Related
- `technique-web-ui`
- `technique-video-processing`
- `technique-visualization`
- `technique-result-capture`