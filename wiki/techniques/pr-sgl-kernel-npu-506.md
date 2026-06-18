---
id: pr-sgl-kernel-npu-506
title: "PR Insight: sgl-project/sgl-kernel-npu #506"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ci
  - packaging
  - deep-ep
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/506"
---

# [CI] Add wheelnext variant wheel build and release workflow for deep_ep

**Repository:** `sgl-project/sgl-kernel-npu`  
**PR:** [#506](https://github.com/sgl-project/sgl-kernel-npu/pull/506)

## Overview

Adds a dedicated CI workflow for building and releasing 'wheelnext' variant wheels for the DeepEP (Deep Expert Parallelism) module, enabling pre-built binary distribution for Ascend NPU users.

## Technical Details

This PR targets the `sgl-project/sgl-kernel-npu` project within the Ascend ecosystem. The change tagged as `ci` improves the overall reliability and usability of the NPU software stack.

## Impact

- **Scope:** Ci
- **Risk:** Low
- **Architectures:** Ascend 910, Ascend 910B
