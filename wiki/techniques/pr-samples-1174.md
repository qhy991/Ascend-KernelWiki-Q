---
id: technique-pr-samples-1174
title: "PR Insight: Ascend/samples #1174"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - video-decode
  - vdec
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1174"
---

# PR Insight: Ascend/samples #1174

**Title:** 【轻量级 PR】：fix vdec variable name bug

## Overview
This PR fixes a variable naming bug in the VDEC (Video Decoder) sample code.

## Technical Significance
Variable naming bugs can cause logical errors, incorrect behavior, or compilation failures. In video decoding pipelines, correct variable usage is critical for proper buffer management, frame tracking, and synchronization between decoding and postprocessing stages.

## Related
- wiki-hardware-unified-buffer
- wiki-hardware-event-sync