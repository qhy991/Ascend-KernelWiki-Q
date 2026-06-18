---
id: technique-pr-cann-ops-adv-338
title: "PR Insight: Ascend/cann-ops-adv #338"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - softmax
  - compilation
  - code-quality
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/338"
---

# PR Insight: Ascend/cann-ops-adv #338

**Title:** 1、fix moe_gating_top_k_softmax_v1_v2 compile warning

## Overview
This PR fixes compilation warnings in the MoE gating top-k softmax V1 and V2 operators. The changes address compiler warnings that could indicate potential issues or code quality problems in the expert gating computation.

## Technical Significance
The MoE gating top-k softmax operator computes expert assignment probabilities and selects the top-k experts for each token. Fixing compilation warnings ensures code quality, prevents potential bugs, and maintains clean builds. The V1 and V2 variants likely represent different implementations with trade-offs between accuracy, performance, or memory usage. Clean compilation without warnings is essential for production-grade operator libraries.

## Related
- `technique-moe-ascendc`
- `technique-softmax-ascendc`
- `technique-top-k-selection`
- `technique-code-quality`