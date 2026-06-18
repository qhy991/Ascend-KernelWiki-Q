---
id: pr-sgl-kernel-npu-560
title: "PR Insight: sgl-project/sgl-kernel-npu #560"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - compilation
  - ascend-a5
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/560"
---

# Solve compilation error on a5

**Repository:** `sgl-project/sgl-kernel-npu`  
**PR:** [#560](https://github.com/sgl-project/sgl-kernel-npu/pull/560)

## Overview

Fixes a compilation error specific to Ascend A5 (Atlas 900A5) hardware by adjusting preprocessor guards and ABI compatibility flags in the kernel build system.

## Technical Details

This PR targets the `sgl-project/sgl-kernel-npu` project within the Ascend ecosystem. The change tagged as `bugfix` improves the overall reliability and usability of the NPU software stack.

## Impact

- **Scope:** Bugfix
- **Risk:** Low
- **Architectures:** Ascend 910, Ascend 910B
