---
id: technique-pr-cann-ops-adv-189
title: "PR Insight: cann-ops-adv #189"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - flash-attention
  - attention
  - bugfix
  - compilation
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/189"
---

# PR Insight: cann-ops-adv #189 - fix fia/ifa/pfa compile custom.run

## Overview
This PR fixes compilation issues with custom.run for FIA (FusedInferAttentionScore), IFA (IncreFlashAttention), and PFA (PromptFlashAttention) operators in the Ascend CANN ops-adv library.

## Technical Significance
Compilation fixes are essential for operator usability. This fix enables correct compilation of the attention operators with custom build configurations, ensuring developers can build and deploy these operators in various inference pipelines on Ascend NPUs.

## Related
- `kernel-flash-attention`
- `kernel-attention`
- `technique-operator-fusion`
- `technique-compilation`