---
id: technique-pr-mindspeed-2138
title: "PR Insight: Ascend/MindSpeed #2138"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - recompute
  - bugfix
  - legacy
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2138"
---

# PR Insight: Ascend/MindSpeed #2138

**Title:** [BUGFIX!] 增加legacy分支下选择性重计算相关说明及warning提示

## Overview
This PR adds documentation and warning messages for selective recompute functionality in the legacy branch of MindSpeed. The change improves user awareness and proper usage of recompute features.

## Technical Significance
Selective recompute is an advanced memory optimization that allows fine-grained control over which activations are recomputed during backward pass. The documentation and warnings help users understand trade-offs and configure recompute correctly on Ascend NPUs. Proper recompute configuration is critical for achieving optimal memory savings without excessive compute overhead. The warnings likely alert users to potential performance pitfalls or configuration errors that could lead to incorrect training results or excessive memory usage.

## Related
- `technique-data-reuse`
- `technique-nz-tiling`