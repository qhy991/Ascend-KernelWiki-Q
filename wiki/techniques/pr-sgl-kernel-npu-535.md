---
id: pr-sgl-kernel-npu-535
title: "PR Insight: sgl-project/sgl-kernel-npu #535"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - precision
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/535"
---

# bugfix: precision ok

**Repository:** `sgl-project/sgl-kernel-npu`  
**PR:** [#535](https://github.com/sgl-project/sgl-kernel-npu/pull/535)

## Overview

Fixes a numerical precision issue in NPU kernel computations, ensuring output accuracy matches reference implementations within acceptable tolerance thresholds.

## Technical Details

This PR targets the `sgl-project/sgl-kernel-npu` project within the Ascend ecosystem. The change tagged as `bugfix` improves the overall reliability and usability of the NPU software stack.

## Impact

- **Scope:** Bugfix
- **Risk:** Low
- **Architectures:** Ascend 910, Ascend 910B
