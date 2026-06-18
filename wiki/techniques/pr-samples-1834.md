---
id: technique-pr-samples-1834
title: "PR Insight: Ascend/samples #1834"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - camera
  - dvpp
  - samples
  - raw
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1834"
---

# PR Insight: Ascend/samples #1834

**Title:** camera level1 级别 sample开发上库，支持imx477 dump raw

## Overview
This PR adds a level-1 camera sample that supports dumping raw image data from the IMX477 sensor. The sample demonstrates how to capture and process raw camera frames on Ascend hardware.

## Technical Significance
Raw image capture capability is fundamental for computer vision pipelines that require access to unprocessed sensor data. The IMX477 is a high-quality camera sensor used in edge AI applications, and this sample provides developers with a reference for integrating camera input with Ascend DVPP processing.

## Related
- `hw-dvpp`
- `wiki-technique-camera-capture`