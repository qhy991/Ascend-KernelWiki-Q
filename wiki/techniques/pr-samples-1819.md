---
id: technique-pr-samples-1819
title: "PR Insight: Ascend/samples #1819"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - venc
  - dvpp
  - samples
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1819"
---

# PR Insight: Ascend/samples #1819

**Title:** venc sample修复bug

## Overview
This PR fixes a bug in the VENC (Video ENCoder) DVPP sample. VENC is used for hardware-accelerated video encoding on Ascend NPUs.

## Technical Significance
Video encoding samples are important for applications that need to generate compressed video outputs, such as video analytics or streaming services. Fixing bugs ensures developers have reliable reference implementations for video encoding workflows on Ascend DVPP hardware.

## Related
- `hw-dvpp`
- `wiki-technique-video-processing`