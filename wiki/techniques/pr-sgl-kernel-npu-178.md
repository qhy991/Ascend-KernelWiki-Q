---
id: technique-pr-sgl-kernel-npu-178
title: "PR Insight: sgl-project/sgl-kernel-npu #178"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - packaging
  - cann
  - versioning
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/178"
---

# PR Insight: sgl-project/sgl-kernel-npu #178

**Title:** optimize deepep setup, package name with cann version

## Overview
Optimizes DeepEP package naming to include CANN version information in the package name. The new format includes git version, CANN version with inner version, Python version, and architecture (e.g., deep_ep-1.0.0+0614abe7.cann.8.2.rc1.b231-cp311-cp311-linux_aarch64.whl).

## Technical Significance
This improvement enhances package management and compatibility tracking by encoding CANN version information directly in the package name. This helps users identify compatible CANN versions and prevents deployment issues caused by version mismatches. The comprehensive versioning includes git commit, CANN version, Python version, and architecture for complete deployment tracking.

## Related
- `wiki-technique-packaging`
- `wiki-technique-versioning`
- `wiki-technique-deployment`