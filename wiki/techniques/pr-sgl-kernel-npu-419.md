---
id: pr-sgl-kernel-npu-419
title: "PR Insight: sgl-project/sgl-kernel-npu #419"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ci
  - build
  - cache
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/419"
---

# feat: route PyTorch deps through internal cache service in CI

**Repository:** `sgl-project/sgl-kernel-npu`  
**PR:** [#419](https://github.com/sgl-project/sgl-kernel-npu/pull/419)

## Overview

Routes PyTorch dependency downloads through an internal cache service during CI builds, reducing external network dependency, improving build reliability, and cutting CI execution time.

## Technical Details

This PR targets the `sgl-project/sgl-kernel-npu` project within the Ascend ecosystem. The change tagged as `ci` improves the overall reliability and usability of the NPU software stack.

## Impact

- **Scope:** Ci
- **Risk:** Low
- **Architectures:** Ascend 910, Ascend 910B
