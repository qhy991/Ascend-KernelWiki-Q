---
id: code-cann-ops-adv-activation
title: "CANN Ops Adv \u2014 Activation Operators"
type: source-code
repo: Ascend/cann-ops-adv
path: src/activation
url: https://gitee.com/ascend/cann-ops-adv/tree/master/src/activation
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- activation
- vector
- ascendc
- cann
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- vector-unit
- unified-buffer
- global-memory
techniques:
- data-reuse
- pipeline-scheduling
kernel_types:
- activation
- elementwise
languages:
- ascendc
- cpp
---

# CANN Ops Adv — Activation Operators

Advanced CANN activation operator source directory. It provides code evidence for vector-unit activation kernels, UB staging, and fused epilogue patterns around transformer MLP blocks.

## Code Location

- Repository: `Ascend/cann-ops-adv`
- Path: `src/activation`
- URL: https://gitee.com/ascend/cann-ops-adv/tree/master/src/activation
