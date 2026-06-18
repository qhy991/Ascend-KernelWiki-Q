---
id: pr-mindspeed-2734
title: "PR Insight: ascend/MindSpeed #2734"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - feature
  - moe
  - load-balancing
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2734"
---

# feat: balanced moe

**Repository:** `ascend/MindSpeed`  
**PR:** [#2734](https://gitee.com/ascend/MindSpeed/pulls/2734)

## Overview

Implements balanced Mixture-of-Experts (MoE) routing that ensures even token distribution across experts, preventing hotspot experts from becoming bottlenecks and improving overall training throughput on Ascend NPU clusters.

## Technical Details

This PR targets the `ascend/MindSpeed` project within the Ascend ecosystem. The change tagged as `feature` improves the overall reliability and usability of the NPU software stack.

## Impact

- **Scope:** Feature
- **Risk:** Low
- **Architectures:** Ascend 910, Ascend 910B
