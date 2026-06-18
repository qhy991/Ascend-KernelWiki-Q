---
id: technique-pr-cann-ops-adv-182
title: "PR Insight: cann-ops-adv #182"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - softmax
  - attention
  - ascendc
  - open-source
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/182"
---

# PR Insight: cann-ops-adv #182 - scaledMaskedSoftmaxV2 开源

## Overview
This PR open-sources the scaledMaskedSoftmaxV2 operator, which performs scaled masked softmax operations for attention with improved implementation over the original version.

## Technical Significance
Open-sourcing this operator enables community adoption and contribution. The V2 version likely includes performance optimizations, better numerical stability, or support for additional masking patterns, improving attention computation on Ascend NPUs.

## Related
- `kernel-softmax`
- `kernel-attention`
- `technique-online-softmax`
- `hw-vector-unit`