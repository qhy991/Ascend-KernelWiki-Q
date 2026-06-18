---
id: technique-pr-samples-2715
title: "PR Insight: Ascend/samples #2715"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - tiling
  - ascendc
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2715"
---

# PR Insight: Ascend/samples #2715

**Title:** change to new tiling definitions

## Overview
This PR updates one or more samples to use new tiling definitions in AscendC. Tiling definitions determine how data is partitioned across the Cube and Vector units, affecting performance and memory access patterns.

## Technical Significance
Tiling is a critical optimization technique in AscendC kernel development. Updating to new tiling definitions can improve performance by better aligning data access patterns with hardware capabilities, reducing bank conflicts, and maximizing Cube unit utilization.

## Related
- technique-nz-tiling
- technique-cube-vector-overlap