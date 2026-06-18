---
id: technique-pr-sgl-kernel-npu-327
title: "PR Insight: sgl-project/sgl-kernel-npu #327"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - build-system
  - deepep
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/327"
---

# PR Insight: sgl-project/sgl-kernel-npu #327

**Title:** Deepep adapt custom cann installation path

## Overview
This PR adapts the DeepEP build system to support custom CANN installation paths. The modifications update CMakeLists.txt and build configuration files across both deepep/ops and deepep/ops2 directories to allow flexible specification of CANN toolkit locations during compilation.

## Technical Significance
Enabling custom CANN installation paths improves deployment flexibility by allowing developers to use non-default CANN installations or multiple CANN versions on the same system. This change supports diverse development and deployment environments where standard CANN paths may not be available or appropriate.

## Related
- `technique-build-optimization`