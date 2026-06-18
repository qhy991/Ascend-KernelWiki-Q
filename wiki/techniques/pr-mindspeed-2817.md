---
id: pr-mindspeed-2817
title: "PR Insight: ascend/MindSpeed #2817"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - gmm
  - backward
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2817"
---

# [mindspore][bugfix] fix bug for npu_gmm_backward

**Repository:** `ascend/MindSpeed`  
**PR:** [#2817](https://gitee.com/ascend/MindSpeed/pulls/2817)

## Overview

Fixes a backward pass bug in `npu_gmm` (Grouped Matrix Multiplication) that caused incorrect gradient computation during MoE training, potentially leading to training divergence on Ascend NPUs.

## Technical Details

This PR targets the `ascend/MindSpeed` project within the Ascend ecosystem. The change tagged as `bugfix` improves the overall reliability and usability of the NPU software stack.

## Impact

- **Scope:** Bugfix
- **Risk:** Low
- **Architectures:** Ascend 910, Ascend 910B
