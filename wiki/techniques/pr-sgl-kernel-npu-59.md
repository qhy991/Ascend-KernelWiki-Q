---
id: technique-pr-sgl-kernel-npu-59
title: "PR Insight: sgl-project/sgl-kernel-npu #59"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - build
  - cmake
  - partial-build
  - infrastructure
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/59"
---

# PR Insight: sgl-project/sgl-kernel-npu #59

**Title:** Support build option deepep/kernels

## Overview
This PR adds granular build options to support independent building of Deep EP and other kernel modules via `-a deepep/kernels` arguments. Updates CMakeLists.txt with conditional build logic and improves build.sh with partial build support.

## Technical Significance
Improves developer experience by enabling faster selective builds for specific modules. Developers can now build only the components they're working on, significantly reducing iteration time during kernel development. This modular build system is essential for large-scale kernel libraries.

## Related
- technique-build-optimization
- technique-cmake
- technique-modular-build