---
id: technique-pr-sgl-kernel-npu-364
title: "PR Insight: sgl-project/sgl-kernel-npu #364"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - bugfix
  - expert-management
  - notify-dispatch
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/364"
---

# PR Insight: sgl-project/sgl-kernel-npu #364

**Title:** Fix the bug that total expert num greater than 256 or local expert num is less than 8

## Overview
This PR fixes bugs in the notify_dispatch and combine normal kernels that caused crashes when total expert count exceeded 256 or local expert count was less than 8. The modifications adjust tiling and memory allocation logic to handle extreme expert distribution scenarios correctly.

## Technical Significance
Fixing expert count boundary issues enables DeepEP to support very large MoE models with hundreds of experts (tested up to 512 total experts with topk=12) and properly handle sparse expert distributions. This ensures robust operation across diverse MoE configurations used in modern large language models.

## Related
- `kernel-notify-dispatch`, `kernel-moe-combine`, `technique-bugfix`