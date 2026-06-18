---
id: technique-pr-mindspeed-2430
title: "PR Insight: Ascend/MindSpeed #2430"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - gqa
  - eod
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2430"
---

# PR Insight: Ascend/MindSpeed #2430

**Title:** EoD 适配GQA，修复EoD重构引入的bug

## Overview
This PR adapts EoD (Expert on Demand) for GQA (Grouped Query Attention) and fixes bugs introduced during EoD refactoring. GQA is an attention optimization that reduces memory and computation by sharing query heads.

## Technical Significance
Enables GQA support in MoE training scenarios, improving memory efficiency and computational performance. The bug fixes ensure correct MoE routing and attention computation after the EoD refactoring.

## Related
- `kernel-attention-ascendc`
- `kernel-flash-attention`
- `technique-moe`
- `technique-gqa`