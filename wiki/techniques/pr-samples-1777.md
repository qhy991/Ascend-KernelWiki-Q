---
id: technique-pr-samples-1777
title: "PR Insight: Ascend/samples #1777"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vdec
  - dvpp
  - samples
  - memory-leak
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1777"
---

# PR Insight: Ascend/samples #1777

**Title:** 修改vdec资源释放问题，dvpp内存泄漏问题

## Overview
This PR fixes resource release issues in the VDEC sample and resolves DVPP memory leaks, ensuring proper cleanup of allocated resources.

## Technical Significance
Memory leaks and improper resource cleanup are critical issues that can cause application crashes or degraded performance over time. Fixing these issues in VDEC samples is essential for long-running video processing applications that must maintain stability without manual intervention.

## Related
- `hw-dvpp`
- `wiki-technique-memory-optimization`
- `wiki-technique-video-processing`