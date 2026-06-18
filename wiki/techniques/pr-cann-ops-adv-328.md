---
id: technique-pr-cann-ops-adv-328
title: "PR Insight: Ascend/cann-ops-adv #328"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pfa
  - tiling
  - compilation
  - graph-optimization
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/328"
---

# PR Insight: Ascend/cann-ops-adv #328

**Title:** fix the tiling interception issue in PFA graph5

## Overview
This PR fixes a tiling interception issue in PFA (likely Pattern Fusion and Acceleration) graph5. The changes address how tiling information is intercepted or processed in this specific graph optimization pattern.

## Technical Significance
Tiling interception issues can lead to incorrect memory layout calculations, suboptimal performance, or compilation errors. PFA graph optimizations are critical for fusing operators and optimizing data movement patterns. This fix ensures that tiling information is correctly passed through the optimization pipeline, enabling proper memory allocation and data movement planning for graph5 patterns. Correct tiling is essential for achieving optimal performance on Ascend's memory hierarchy.

## Related
- `technique-graph-optimization`
- `technique-tiling-optimization`
- `technique-pattern-fusion`
- `technique-compilation`