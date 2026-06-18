---
id: technique-pr-cann-ops-adv-191
title: "PR Insight: cann-ops-adv #191"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - routing
  - bugfix
  - correctness
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/191"
---

# PR Insight: cann-ops-adv #191 - fix moeinitrouting unused param

## Overview
This PR fixes an issue with unused parameters in the MoeInitRouting operator, addressing compiler warnings or potential runtime issues in MoE routing initialization.

## Technical Significance
Unused parameter fixes improve code quality and eliminate compiler warnings. The fix ensures cleaner code and may address subtle issues with parameter handling, improving robustness of MoE routing initialization on Ascend NPUs.

## Related
- `kernel-moe`
- `kernel-topk`
- `technique-debugging`
- `hw-vector-unit`