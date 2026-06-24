---
id: technique-pr-samples-1649
title: "PR Insight: Ascend/samples #1649"
type: wiki-technique
architectures:
  - ascend310p
  - ascend310p
tags:
  - samples
  - 310b
  - video-colorization
  - porting
  - computer-vision
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1649"
---

# PR Insight: Ascend/samples #1649

**Title:** 310B样例迁移-黑白视频上色

## Overview
This PR ports the black-and-white video colorization sample to the Ascend 310B platform, adapting the generative vision application for edge deployment.

## Technical Significance
Video colorization is a generative task that adds color to monochrome video, useful for restoring archival footage and enhancing video content. Porting to 310B shows how to optimize generative models for edge deployment, balancing quality and latency on resource-constrained hardware.

## Related
- wiki-hardware-ascend310p
- technique-generative-models