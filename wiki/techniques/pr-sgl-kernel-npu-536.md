---
id: pr-sgl-kernel-npu-536
title: "PR Insight: sgl-project/sgl-kernel-npu #536"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ci
  - testing
  - cann
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/536"
---

# Add cann9.0.0 and a2 to dailytest and pr test

**Repository:** `sgl-project/sgl-kernel-npu`  
**PR:** [#536](https://github.com/sgl-project/sgl-kernel-npu/pull/536)

## Overview

Extends CI test matrix to include CANN 9.0.0 and Ascend A2 (Atlas 200) hardware targets, ensuring kernel correctness across a broader range of Ascend SDK versions and chip architectures.

## Technical Details

This PR targets the `sgl-project/sgl-kernel-npu` project within the Ascend ecosystem. The change tagged as `ci` improves the overall reliability and usability of the NPU software stack.

## Impact

- **Scope:** Ci
- **Risk:** Low
- **Architectures:** Ascend 910, Ascend 910B
