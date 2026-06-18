---
id: technique-pr-sgl-kernel-npu-53
title: "PR Insight: sgl-project/sgl-kernel-npu #53"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - build
  - performance
  - cmake
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/53"
---

# PR Insight: sgl-project/sgl-kernel-npu #53

**Title:** Support only build deepep

## Overview
This PR adds support for building only the Deep EP component via `bash build.sh -a deepep`, reducing build time from 109s to 71s. Updates CMakeLists.txt and build.sh to enable selective compilation.

## Technical Significance
Improves developer productivity by enabling faster incremental builds when only Deep EP changes are needed. The 35% build time reduction accelerates iteration during Deep EP kernel development, essential for rapid prototyping and optimization cycles.

## Related
- technique-build-optimization
- technique-cmake