---
id: pr-mindspeed-2827
title: "PR Insight: ascend/MindSpeed #2827"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - distributed
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2827"
---

# fix: fix get_full_args

**Repository:** `ascend/MindSpeed`  
**PR:** [#2827](https://gitee.com/ascend/MindSpeed/pulls/2827)

## Overview

Fixes the `get_full_args` utility function used during FSDP parameter gathering, correcting argument handling that could cause silent data corruption or crashes during checkpoint save/load on multi-NPU setups.

## Technical Details

This PR targets the `ascend/MindSpeed` project within the Ascend ecosystem. The change tagged as `bugfix` improves the overall reliability and usability of the NPU software stack.

## Impact

- **Scope:** Bugfix
- **Risk:** Low
- **Architectures:** Ascend 910, Ascend 910B
